"""
Build the `m5` dataset of skforecast (m5_daily.parquet, published on Hugging
Face as skforecast/m5_daily).

Daily unit sales of 3049 products in 10 Walmart stores of California, Texas and
Wisconsin, from the M5 Accuracy competition, with the product hierarchy, weekly
sell prices, calendar events and SNAP days. Walmart provided the data to the
organizers of the competition (University of Nicosia), who published the whole
dataset, the 28 days of the test period included, in a public folder linked
from their repository https://github.com/Mcompetitions/M5-methods (subfolder
`Dataset/`). This script only uses that release.

Output: <workdir>/out/m5_daily.parquet. Long format, one row per series and
day: 30490 series x 1969 days (d_1 to d_1969, 2011-01-29 to 2016-06-19). Rows
are sorted by date and, within each date, in the order of the series of
sales_train_evaluation.csv. The raw files are downloaded to <workdir>/raw/,
outside the repository, and the script stops if the sha256 of any of them is
not the expected one.

Run it with pandas 2.x, as the published file: pandas 3 writes other metadata
for the string columns, and the file must be read in the same way by pandas 2
and pandas 3.

If the download from Google Drive fails, download the files by hand into
<workdir>/raw/, for example with `gdown <id> -O <workdir>/raw/<file>` (ids in
FILES below). Their sha256 is checked anyway.

Usage, from the root of the repository (needs numpy, pandas 2.x and pyarrow):
    python scripts/build_m5_daily.py --workdir C:/tmp/m5_daily
    python scripts/build_m5_daily.py --workdir C:/tmp/m5_daily --download-only
"""

import argparse
import hashlib
import platform
import shutil
import tempfile
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

URL = "https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t"
# name: (Google Drive id, sha256)
FILES = {
    "sales_train_evaluation.csv": (
        "1-khP8tp1gRTfaQQV_PlKd6R_3Mw5KiBw",
        "c21a519596680feb86f27a9e62f6c8b583f8be60c2c195f080ae8ca2990af2b7",
    ),
    "sales_test_evaluation.csv": (
        "1Bj7Xj15yn4j6-BM_mpSmOVTV0c2ihEdo",
        "73773250dd7f7464f7a1bf3a54874dc7fc8cbb49885cd0bf1efe09bf48fd930d",
    ),
    "calendar.csv": (
        "1eeU8Me44yzgWsDD0dYrX4xVOixil_H4u",
        "568d0fe5f41790142379698732908e4e57432c1c6396f3f59fb880a9c2b54231",
    ),
    "sell_prices.csv": (
        "1YKo2D7rpg9y5L-qaidUjyJaKvTIR0rMI",
        "5c7cf045b1abbdc8d5007809c40b3682c5216075937f93e2cef01caddc4a30d9",
    ),
}
WORKDIR = Path(tempfile.gettempdir()) / "m5_daily"

N_SERIES = 30490
N_DAYS = 1969
N_DAYS_TRAIN = 1941
FIRST_DATE = "2011-01-29"
LAST_DATE = "2016-06-19"
TEST_START = "2016-05-23"
HIERARCHY = ["item_id", "dept_id", "cat_id", "store_id", "state_id"]
EVENTS = ["event_name_1", "event_type_1", "event_name_2", "event_type_2"]
SNAP = ["snap_CA", "snap_TX", "snap_WI"]

EXPECTED_SCHEMA = pa.schema(
    [
        ("id", pa.dictionary(pa.int16(), pa.string())),
        ("datetime", pa.timestamp("ns")),
        ("item_id", pa.dictionary(pa.int16(), pa.string())),
        ("dept_id", pa.dictionary(pa.int8(), pa.string())),
        ("cat_id", pa.dictionary(pa.int8(), pa.string())),
        ("store_id", pa.dictionary(pa.int8(), pa.string())),
        ("state_id", pa.dictionary(pa.int8(), pa.string())),
        ("sales", pa.int16()),
        *[(column, pa.string()) for column in EVENTS],
        *[(column, pa.int8()) for column in SNAP],
        ("sell_price", pa.float64()),
    ]
)
EXPECTED_TOTAL_SALES = 68_156_315
EXPECTED_DAILY_SALES = {
    "2011-01-29": 32_631,
    "2016-04-25": 38_793,
    "2016-05-22": 54_338,
    "2016-05-23": 40_385,
    "2016-06-19": 47_065,
}
EXPECTED_PRICE_NULLS = 12_299_413
EXPECTED_PRICE_SUM = 210_547_738.89


def check(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Check failed: {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(name: str, file_id: str, path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {name}", flush=True)
    part = path.with_name(path.name + ".part")
    request = urllib.request.Request(
        URL.format(id=file_id), headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        if response.headers.get("Content-Type", "").startswith("text/html"):
            raise SystemExit(
                f"Google Drive returned a web page instead of {name}: download it "
                f"by hand into {path.parent} (see the docstring)."
            )
        with open(part, "wb") as file:
            shutil.copyfileobj(response, file, length=2**20)
    part.replace(path)


def fetch_raw_files(raw: Path) -> None:
    mismatches = []
    for name, (file_id, expected) in FILES.items():
        path = raw / name
        download(name, file_id, path)
        digest = sha256(path)
        print(f"{name}: {path.stat().st_size:,} bytes, sha256 {digest}", flush=True)
        if digest != expected:
            mismatches.append(f"{name}: expected {expected}, got {digest}")
    if mismatches:
        raise SystemExit("sha256 mismatch:\n" + "\n".join(mismatches))


def read_sales(raw: Path) -> tuple[pd.DataFrame, np.ndarray]:
    """
    Series (id and hierarchy, in the order of sales_train_evaluation.csv) and
    their sales, a matrix of shape (series, days).
    """
    days_train = [f"d_{i}" for i in range(1, N_DAYS_TRAIN + 1)]
    days_test = [f"d_{i}" for i in range(N_DAYS_TRAIN + 1, N_DAYS + 1)]

    # The files of the organizers' release have no id column: it is built as
    # item_id + "_" + store_id + "_evaluation", and the test file is joined to
    # the train file by id, never by position
    train = pd.read_csv(raw / "sales_train_evaluation.csv")
    check(
        list(train.columns) == [*HIERARCHY, *days_train],
        "columns of sales_train_evaluation.csv are the hierarchy and d_1 to d_1941",
    )
    check(len(train) == N_SERIES, f"{N_SERIES} series in sales_train_evaluation.csv")
    train.insert(0, "id", train["item_id"] + "_" + train["store_id"] + "_evaluation")
    check(train["id"].is_unique, "unique ids in sales_train_evaluation.csv")

    test = pd.read_csv(raw / "sales_test_evaluation.csv")
    check(
        list(test.columns) == [*HIERARCHY, *days_test],
        "columns of sales_test_evaluation.csv are the hierarchy and d_1942 to d_1969",
    )
    test.index = test["item_id"] + "_" + test["store_id"] + "_evaluation"
    check(test.index.is_unique, "unique ids in sales_test_evaluation.csv")
    check(
        set(test.index) == set(train["id"]),
        "same series in sales_train_evaluation.csv and sales_test_evaluation.csv",
    )
    test = test.loc[train["id"]]
    for column in HIERARCHY:
        check(
            (test[column].to_numpy() == train[column].to_numpy()).all(),
            f"same {column} of each series in the train and test files",
        )

    sales = np.concatenate(
        [train[days_train].to_numpy(), test[days_test].to_numpy()], axis=1
    )
    check(np.issubdtype(sales.dtype, np.integer), "sales without missing values")
    check(
        sales.min() >= 0 and sales.max() <= np.iinfo(np.int16).max,
        "sales between 0 and the maximum of int16",
    )
    return train[["id", *HIERARCHY]], sales.astype(np.int16)


def read_calendar(raw: Path) -> pd.DataFrame:
    """
    One row per day, d_1 (2011-01-29) to d_1969 (2016-06-19). The calendar of
    the organizers' release has no `d` column: day d_i is the row i.
    """
    calendar = pd.read_csv(raw / "calendar.csv")
    calendar["date"] = pd.to_datetime(calendar["date"], format="%Y-%m-%d")
    check(
        calendar["date"].tolist()
        == pd.date_range(FIRST_DATE, LAST_DATE, freq="D").tolist(),
        f"calendar.csv has consecutive days from {FIRST_DATE} to {LAST_DATE}",
    )
    for column in SNAP:
        check(
            set(calendar[column].unique()) <= {0, 1},
            f"{column} only takes the values 0 and 1",
        )
    return calendar


def read_prices(raw: Path, series: pd.DataFrame, calendar: pd.DataFrame) -> np.ndarray:
    """
    Sell price of each series and day, a matrix of shape (series, days) with
    NaN when the product was not on sale that week.
    """
    prices = pd.read_csv(raw / "sell_prices.csv")
    check(
        not prices.duplicated(["store_id", "item_id", "wm_yr_wk"]).any(),
        "one price per store, item and week in sell_prices.csv",
    )
    check(
        prices["sell_price"].notna().all() and (prices["sell_price"] > 0).all(),
        "positive prices in sell_prices.csv",
    )
    series_key = pd.Index(series["store_id"] + "|" + series["item_id"])
    rows = series_key.get_indexer(prices["store_id"] + "|" + prices["item_id"])
    check((rows >= 0).all(), "every store and item of sell_prices.csv is a series")
    weeks = pd.Index(np.sort(calendar["wm_yr_wk"].unique()))
    columns = weeks.get_indexer(prices["wm_yr_wk"])
    check((columns >= 0).all(), "every week of sell_prices.csv is in calendar.csv")

    price_week = np.full((len(series), len(weeks)), np.nan)
    price_week[rows, columns] = prices["sell_price"].to_numpy()
    return price_week[:, weeks.get_indexer(calendar["wm_yr_wk"])]


def build(raw: Path) -> tuple[pd.DataFrame, pd.Series, pd.Series]:
    """
    Long-format DataFrame, and the ids and dates read from the raw files, to
    validate the order of the rows of the written file.
    """
    series, sales = read_sales(raw)
    calendar = read_calendar(raw)
    price = read_prices(raw, series, calendar)

    # Row r is the day r // N_SERIES of the series r % N_SERIES
    def per_series(values: pd.Series) -> pd.Categorical:
        categorical = pd.Categorical(values)
        return pd.Categorical.from_codes(
            np.tile(categorical.codes, N_DAYS), categorical.categories
        )

    def per_day(values: np.ndarray) -> np.ndarray:
        return np.repeat(values, N_SERIES)

    data = {"id": per_series(series["id"])}
    data["datetime"] = per_day(calendar["date"].to_numpy().astype("datetime64[ns]"))
    for column in HIERARCHY:
        data[column] = per_series(series[column])
    data["sales"] = sales.T.ravel()
    for column in EVENTS:
        values = calendar[column].to_numpy(dtype=object)
        values[pd.isna(values)] = None
        data[column] = per_day(values)
    for column in SNAP:
        data[column] = per_day(calendar[column].to_numpy().astype(np.int8))
    data["sell_price"] = price.T.ravel()
    return pd.DataFrame(data, copy=False), series["id"], calendar["date"]


def validate(path: Path, series_ids: pd.Series, dates: pd.Series) -> None:
    """
    Check the written file, read back from disk.
    """
    schema = pq.read_schema(path).remove_metadata()
    check(schema.equals(EXPECTED_SCHEMA), f"schema of the file:\n{schema}")
    print("Schema: ok", flush=True)

    df = pd.read_parquet(path, columns=["id", "datetime", "sales", "sell_price"])
    check(len(df) == N_SERIES * N_DAYS, f"{N_SERIES * N_DAYS:,} rows")
    check(df["id"].nunique() == N_SERIES, f"{N_SERIES} ids")
    check(df["datetime"].nunique() == N_DAYS, f"{N_DAYS} dates")

    # Position of each row in sales_train_evaluation.csv and day number
    series_position = pd.Index(series_ids).get_indexer(df["id"].cat.categories)
    check((series_position >= 0).all(), "ids of the file are the input series")
    series_index = series_position[df["id"].cat.codes.to_numpy()]
    day_index = pd.Index(dates).get_indexer(df["datetime"])
    check((day_index >= 0).all(), "dates of the file are the calendar dates")
    check(
        np.array_equal(series_index, np.tile(np.arange(N_SERIES), N_DAYS))
        and np.array_equal(day_index, np.repeat(np.arange(N_DAYS), N_SERIES)),
        "rows sorted by date and, within each date, in the order of the series",
    )
    counts = np.bincount(day_index.astype(np.int64) * N_SERIES + series_index)
    check(counts.max() == 1, "no duplicated (id, datetime)")
    rows_per_id = np.bincount(series_index, minlength=N_SERIES)
    check((rows_per_id == N_DAYS).all(), f"{N_DAYS} rows per id")
    print(
        f"Shape: {len(df):,} rows, {N_SERIES} ids, {N_DAYS} dates "
        f"({dates.iloc[0]:%Y-%m-%d} to {dates.iloc[-1]:%Y-%m-%d}), "
        f"{N_DAYS} rows per id, no duplicates, sorted: ok",
        flush=True,
    )

    check(df["sales"].isna().sum() == 0, "sales without missing values")
    total_sales = int(df["sales"].to_numpy().sum(dtype=np.int64))
    check(total_sales == EXPECTED_TOTAL_SALES, f"total sales {total_sales:,}")
    print(f"Total sales: {total_sales:,}: ok", flush=True)

    daily_sales = pd.Series(
        df["sales"].to_numpy().reshape(N_DAYS, N_SERIES).sum(axis=1, dtype=np.int64),
        index=pd.DatetimeIndex(dates),
    )
    for date, expected in EXPECTED_DAILY_SALES.items():
        value = int(daily_sales[date])
        check(value == expected, f"sales of {date}: {value:,}")
        print(f"Sales of {date}: {value:,}: ok", flush=True)

    price_nulls = int(df["sell_price"].isna().sum())
    price_sum = round(float(df["sell_price"].sum()), 2)
    check(price_nulls == EXPECTED_PRICE_NULLS, f"{price_nulls:,} null prices")
    check(price_sum == EXPECTED_PRICE_SUM, f"sum of prices {price_sum:,.2f}")
    print(f"sell_price: {price_nulls:,} nulls, sum {price_sum:,.2f}: ok", flush=True)

    price = df["sell_price"].to_numpy().reshape(N_DAYS, N_SERIES)
    test_days = (dates >= TEST_START).to_numpy()
    test_price = price[test_days]
    series_without_price = int(np.isnan(test_price).all(axis=0).sum())
    check(
        series_without_price == 0,
        f"{series_without_price} series without price from {TEST_START}",
    )
    print(
        f"sell_price from {TEST_START} to {LAST_DATE}: no series without price "
        f"({int(np.isnan(test_price).sum())} null values): ok",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--workdir", type=Path, default=WORKDIR)
    parser.add_argument(
        "--download-only",
        action="store_true",
        help="Download the raw files and check their sha256, without building.",
    )
    args = parser.parse_args()
    raw = args.workdir / "raw"
    output = args.workdir / "out" / "m5_daily.parquet"

    print(
        f"Python {platform.python_version()}, numpy {np.__version__}, "
        f"pandas {pd.__version__}, pyarrow {pa.__version__}",
        flush=True,
    )
    fetch_raw_files(raw)
    if args.download_only:
        return
    check(
        pd.__version__.startswith("2."),
        f"run with pandas 2.x (found {pd.__version__}), see the docstring",
    )

    df, series_ids, dates = build(raw)
    print(f"Built {df.shape}", flush=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Explicit schema, so that the types do not depend on the data
    df.to_parquet(output, engine="pyarrow", schema=EXPECTED_SCHEMA)
    del df

    validate(output, series_ids, dates)
    metadata = pq.read_metadata(output)
    print(
        f"Saved {output}: {output.stat().st_size:,} bytes, "
        f"{metadata.num_row_groups} row groups, sha256 {sha256(output)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
