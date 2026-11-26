---
license: other
license_name: m5-organizers-public-release
license_link: https://github.com/Mcompetitions/M5-methods
pretty_name: M5 daily sales
task_categories:
- time-series-forecasting
tags:
- time-series
- forecasting
- retail
- sales
- hierarchical
- m5
size_categories:
- 10M<n<100M
---

# M5 daily sales

Daily unit sales of the M5 Accuracy competition: 3049 products sold in 10 Walmart stores of California, Texas and Wisconsin (30490 product and store series), with the product hierarchy (item, department, category), the store hierarchy (store, state), weekly sell prices, calendar events and SNAP days.

The file `m5_daily.parquet` is in long format: one row per series and day, 30490 series x 1969 days = 60,034,810 rows, from 2011-01-29 to 2016-06-19. Rows are sorted by date and, within each date, in the order of the series of the organizers' file `sales_train_evaluation.csv`.

## Competition periods

| Period | Days | Dates |
|---|---|---|
| Training | d_1 to d_1913 | 2011-01-29 to 2016-04-24 |
| Validation | d_1914 to d_1941 | 2016-04-25 to 2016-05-22 |
| Test | d_1942 to d_1969 | 2016-05-23 to 2016-06-19 |

The test period is the one used to rank the competition (evaluation phase), so models trained up to 2016-05-22 can be compared with the published results.

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | category | Series id, `<item_id>_<store_id>_evaluation`, as in the evaluation phase of the competition. |
| `datetime` | datetime64[ns] | Day (date without time). |
| `item_id` | category | Product, for example `HOBBIES_1_001`. |
| `dept_id` | category | Department of the product (7 departments). |
| `cat_id` | category | Category of the product: `FOODS`, `HOBBIES` or `HOUSEHOLD`. |
| `store_id` | category | Store: `CA_1` to `CA_4`, `TX_1` to `TX_3`, `WI_1` to `WI_3`. |
| `state_id` | category | State of the store: `CA`, `TX` or `WI`. |
| `sales` | int16 | Units sold that day. No missing values. |
| `event_name_1` | string | Name of the event of the day (sporting, cultural, national or religious), null if there is none. |
| `event_type_1` | string | Type of `event_name_1`, null if there is no event. |
| `event_name_2` | string | Name of a second event on the same day, null if there is none. |
| `event_type_2` | string | Type of `event_name_2`, null if there is no second event. |
| `snap_CA` | int8 | 1 if purchases with SNAP benefits (Supplemental Nutrition Assistance Program) were allowed that day in California, 0 otherwise. |
| `snap_TX` | int8 | Same for Texas. |
| `snap_WI` | int8 | Same for Wisconsin. |
| `sell_price` | float64 | Weekly price of the product in the store (USD). Null when the product was not on sale that week, for example before it was first sold. |

## Source

The M5 competition was organized by the University of Nicosia (Makridakis Open Forecasting Center). Walmart provided the data to the organizers, who published the whole dataset after the competition, the sales of the test period included, in a public folder (subfolder `Dataset/`) linked from their repository https://github.com/Mcompetitions/M5-methods.

This file is built only from that release (`sales_train_evaluation.csv`, `sales_test_evaluation.csv`, `calendar.csv` and `sell_prices.csv`) by the script `scripts/build_m5_daily.py` of https://github.com/skforecast/skforecast-datasets, which checks the sha256 of the files and the totals of the result. Only the format changes: the values are those of the organizers' files.

## Citation

Makridakis, S., Spiliotis, E. and Assimakopoulos, V. (2022). M5 accuracy competition: Results, findings, and conclusions. *International Journal of Forecasting*, 38(4), 1346-1364. https://doi.org/10.1016/j.ijforecast.2021.11.013

```bibtex
@article{makridakis2022m5,
  title   = {M5 accuracy competition: Results, findings, and conclusions},
  author  = {Makridakis, Spyros and Spiliotis, Evangelos and Assimakopoulos, Vassilios},
  journal = {International Journal of Forecasting},
  volume  = {38},
  number  = {4},
  pages   = {1346-1364},
  year    = {2022},
  doi     = {10.1016/j.ijforecast.2021.11.013}
}
```

## Use

Intended for research and educational use.

The data belongs to its authors and is distributed under their terms, not under the license of skforecast: skforecast does not grant any license on it, open or otherwise. For any other use, contact the organizers of the M5 competition (https://github.com/Mcompetitions/M5-methods).

## Example

With [skforecast](https://skforecast.org):

```python
from skforecast.datasets import fetch_dataset

data = fetch_dataset("m5")
```

`fetch_dataset` sets `datetime` as the index of the DataFrame. The whole dataset takes about 8 GB of memory with pandas 2 (about 4 GB with pandas 3, which stores the event columns as `str`). To load only some columns, pass them to `kwargs_read`, including `datetime`:

```python
data = fetch_dataset(
    "m5", kwargs_read={"columns": ["id", "datetime", "sales", "sell_price"]}
)
```

Without skforecast:

```python
import pandas as pd

data = pd.read_parquet(
    "https://huggingface.co/datasets/skforecast/m5_daily/resolve/main/m5_daily.parquet"
)
```
