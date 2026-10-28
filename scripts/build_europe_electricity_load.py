"""
Build the `europe_electricity_load` dataset for skforecast-datasets.

Hourly electricity load (MW) of Spain, Portugal, France, Italy and Germany
from the Energy-Charts API (Fraunhofer ISE), licensed under CC BY 4.0.
Values reported every 15 minutes are averaged to hourly.

National public holidays (Nager.Date API, `global` holidays only) are added
as one binary column per country, `holiday_<country>`, using the local date
of each country (the index is UTC).

Output: data/europe_electricity_load.csv (UTC index). Raw API responses are
cached in the system temporary directory, outside the repository.

Energy-Charts may revise past values, so a new run can differ slightly from
the published CSV, which is the reference used by skforecast.

Usage, from the root of the repository:
    python scripts/build_europe_electricity_load.py
"""

import json
import tempfile
import time
import urllib.request
from pathlib import Path

import pandas as pd

URL = "https://api.energy-charts.info/public_power?country={cc}&start={start}&end={end}"
URL_HOLIDAYS = "https://date.nager.at/api/v3/PublicHolidays/{year}/{cc}"
COUNTRIES = {
    "es": "spain",
    "pt": "portugal",
    "fr": "france",
    "it": "italy",
    "de": "germany",
}
TIMEZONES = {
    "es": "Europe/Madrid",
    "pt": "Europe/Lisbon",
    "fr": "Europe/Paris",
    "it": "Europe/Rome",
    "de": "Europe/Berlin",
}
YEARS = range(2019, 2026)
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "europe_electricity_load.csv"
RAW = Path(tempfile.gettempdir()) / "europe_electricity_load_raw"


def fetch_json(url: str, cache: Path) -> object:
    # Raw responses are cached: the API answers 429 to quick bursts
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        for wait in (10, 30, 60, 120, 240):
            try:
                with urllib.request.urlopen(url, timeout=120) as response:
                    cache.write_bytes(response.read())
                break
            except urllib.error.HTTPError as error:
                if error.code != 429:
                    raise
                time.sleep(wait)
        time.sleep(5)
    return json.loads(cache.read_text())


def fetch_load(cc: str, year: int) -> pd.Series:
    url = URL.format(cc=cc, start=f"{year}-01-01", end=f"{year}-12-31")
    data = fetch_json(url, RAW / f"{cc}_{year}.json")
    load = next(p for p in data["production_types"] if p["name"] == "Load")
    index = pd.to_datetime(data["unix_seconds"], unit="s", utc=True)
    return pd.Series(load["data"], index=index, dtype=float)


def holiday_flag(cc: str, index: pd.DatetimeIndex) -> pd.Series:
    days = set()
    for year in YEARS:
        url = URL_HOLIDAYS.format(year=year, cc=cc.upper())
        holidays = fetch_json(url, RAW / f"holidays_{cc}_{year}.json")
        days.update(pd.Timestamp(h["date"]) for h in holidays if h["global"])
    local_date = index.tz_convert(TIMEZONES[cc]).tz_localize(None).normalize()
    return pd.Series(local_date.isin(days).astype(int), index=index)


def main() -> None:
    series = {}
    for cc, name in COUNTRIES.items():
        parts = []
        for year in YEARS:
            parts.append(fetch_load(cc, year))
        s = pd.concat(parts)
        s = s[~s.index.duplicated()].sort_index()
        series[name] = s.resample("h").mean()
        print(f"{name}: {len(series[name])} hours, {series[name].isna().sum()} NaN")

    data = pd.DataFrame(series).round(1)
    # The API end date is exclusive: the last hour comes empty for most countries
    data = data.loc["2019-01-01":"2025-12-31 22:00"]
    for cc, name in COUNTRIES.items():
        data[f"holiday_{name}"] = holiday_flag(cc, data.index)
    data.index = data.index.tz_localize(None)
    data.index.name = "datetime"
    OUTPUT.parent.mkdir(exist_ok=True)
    data.to_csv(OUTPUT)
    print(f"Saved {data.shape} to {OUTPUT}")


if __name__ == "__main__":
    main()
