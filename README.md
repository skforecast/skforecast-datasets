# skforecast-datasets

This repository contains datasets used in the skforecast library. It also contains datasets used in related tutorials.

All datasets included have a short description as well as the original source. They can be downloaded from the url of each dataset (the largest ones are hosted on Hugging Face) or by using the `fetch_dataset()` function from the skforecast library.

```python
from skforecast.datasets import fetch_dataset
data = fetch_dataset(name="h2o")
```

## Datasets

### h2o

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/h2o.csv
+ sep: ','
+ index_col: fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly expenditure ($AUD) on corticosteroid drugs that the Australian health system had between 1991 and 2008.
+ source: Hyndman R (2023). fpp3: Data for Forecasting: Principles and Practice (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.

### h2o_exog

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/h2o_exog.csv
+ sep: ','
+ index_col: fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly expenditure ($AUD) on corticosteroid drugs that the Australian health system had between 1991 and 2008. Two additional variables (exog_1, exog_2) are simulated.
+ source: Hyndman R (2023). fpp3: Data for Forecasting: Principles and Practice (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.

### fuel_consumption

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/consumos-combustibles-mensual.csv
+ sep: ','
+ index_col: Fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly fuel consumption (tons) in Spain from 1969-01-01 to 2022-08-01.
+ source: Obtained from Corporación de Reservas Estratégicas de Productos Petrolíferos and Corporación de Derecho Público tutelada por el Ministerio para la Transición Ecológica y el Reto Demográfico. https://www.cores.es/es/estadisticas

### items_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/simulated_items_sales.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Simulated time series for the sales of 3 different items.
+ source: Simulated data.

### air_quality_valencia

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/air_quality_valencia.csv
+ sep: ','
+ index_col: datetime
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly measures of several air chemical pollutants at Valencia city (Avd. Francia) from 2019-01-01 to 2023-12-31. Including the following variables: pm2.5 (µg/m³), CO (mg/m³), NO (µg/m³), NO2 (µg/m³), PM10 (µg/m³), NOx (µg/m³), O3 (µg/m³), Veloc. (m/s), Direc. (degrees), SO2 (µg/m³).
+ source: Red de Vigilancia y Control de la Contaminación Atmosférica, 46250047-València - Av. França, https://mediambient.gva.es/es/web/calidad-ambiental/datos-historicos.

### air_quality_valencia_no_missing

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/air_quality_valencia_no_missing.csv
+ sep: ','
+ index_col: datetime
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly measures of several air chemical pollutants at Valencia city (Avd. Francia) from 2019-01-01 to 2023-12-31. Including the following variables: pm2.5 (µg/m³), CO (mg/m³), NO (µg/m³), NO2 (µg/m³), PM10 (µg/m³), NOx (µg/m³), O3 (µg/m³), Veloc. (m/s), Direc. (degrees), SO2 (µg/m³). Missing values have been imputed using linear interpolation.
+ source: Red de Vigilancia y Control de la Contaminación Atmosférica, 46250047-València - Av. França, https://mediambient.gva.es/es/web/calidad-ambiental/datos-historicos.

### website_visits

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/visitas_por_dia_web_cienciadedatos.csv
+ sep: ','
+ index_col: date
+ date_format: %d/%m/%y
+ freq: D
+ file_type: csv
+ description: Daily visits to the cienciadedatos.net website registered with the google analytics service.
+ source: Amat Rodrigo, J. (2021). cienciadedatos.net (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.10006330

### bike_sharing

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_dataset_clean.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### bike_sharing_extended_features

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_extended_features.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling. Additionally, the dataset was enriched by introducing supplementary features. Additions include calendar-based variables (day of the week, hour of the day, month, etc.), indicators for sunlight, rolling temperature averages, and polynomial features generated from variable pairs. All cyclic variables are encoded using sine and cosine transformations.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### australia_tourism

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/australia_tourism.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d
+ freq: QS
+ file_type: csv
+ description: Quarterly overnight trips (in thousands) from 1998 Q1 to 2017 Q4 across Australia. The tourism regions are formed through the aggregation of Statistical Local Areas (SLAs) which are defined by the various State and Territory tourism authorities according to their research and marketing needs. Long format: one row per region, state, purpose and quarter (304 series).
+ source: Wang, E, D Cook, and RJ Hyndman (2020). A new tidy data structure to support exploration and modeling of temporal data, Journal of Computational and Graphical Statistics, 29:3, 466-478, doi:10.1080/10618600.2019.1695624.

### uk_daily_flights

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/uk_daily_flights.csv
+ sep: ','
+ index_col: Date
+ date_format: %d/%m/%Y
+ freq: D
+ file_type: csv
+ description: Daily number of flights in UK from 02/01/2019 to 23/01/2022.
+ source: Experimental statistics published as part of the Economic activity and social change in the UK, real-time indicators release, Published 27 January 2022. Daily flight numbers are available in the dashboard provided by the European Organisation for the Safety of Air Navigation (EUROCONTROL). https://www.ons.gov.uk/economy/economicoutputandproductivity/output/bulletins/economicactivityandsocialchangeintheukrealtimeindicators/latest

### wikipedia_visits

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/wikipedia_visits.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Log daily page views for the Wikipedia page for Peyton Manning. Scraped data using the Wikipediatrend package in R.
+ source: https://github.com/facebook/prophet/blob/main/examples/example_wp_log_peyton_manning.csv

### vic_electricity

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/vic_electricity.csv
+ sep: ','
+ index_col: Time
+ date_format: %Y-%m-%dT%H:%M:%SZ
+ freq: 30min
+ file_type: csv
+ description: Half-hourly electricity demand for Victoria, Australia. `Time` is in UTC (suffix Z, parsed as a naive datetime); `Date` and `Holiday` refer to local time in Melbourne (UTC+10, UTC+11 in summer).
+ source: O'Hara-Wild M, Hyndman R, Wang E, Godahewa R (2022). tsibbledata: Diverse Datasets for 'tsibble'. https://tsibbledata.tidyverts.org/, https://github.com/tidyverts/tsibbledata/. https://tsibbledata.tidyverts.org/reference/vic_elec.html

### vic_electricity_classification

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/vic_electricity_classification.csv
+ sep: ','
+ index_col: Time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly electricity demand for Victoria, Australia classified into three categories: 'low', 'medium' and 'high' according to the 20th and 80th percentiles. The dataset also includes temperature, holiday indicator and hour of the day as features.
+ source: O'Hara-Wild M, Hyndman R, Wang E, Godahewa R (2022). tsibbledata: Diverse Datasets for 'tsibble'. https://tsibbledata.tidyverts.org/, https://github.com/tidyverts/tsibbledata/. https://tsibbledata.tidyverts.org/reference/vic_elec.html

### store_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/store_sales.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: This dataset contains 913,000 sales transactions from 2013-01-01 to 2017-12-31 for 50 products (SKU) in 10 stores. Long format: one row per store, item and date.
+ source: The original data was obtained from: inversion. (2018). Store Item Demand Forecasting Challenge. Kaggle. https://kaggle.com/competitions/demand-forecasting-kernels-only

### bicimad

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bicimad_users.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: This dataset contains the daily users of the bicycle rental service (BiciMad) in the city of Madrid (Spain) from 2014-06-23 to 2022-09-30.
+ source: The original data was obtained from: Portal de datos abiertos del Ayuntamiento de Madrid https://datos.madrid.es/portal/site/egob

### m4_daily

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_daily.parquet
+ sep:
+ index_col: timestamp
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: D
+ file_type: parquet
+ description: Time series with daily frequency from the M4 competition. Timestamps are artificial (the M4 series have no real dates): all at 12:00 and spanning 1959 to 2039. Long format: one row per series and timestamp.
+ source: Monash Time Series Forecasting Repository (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks. Raw data, available in .tsf format, has been converted to Pandas format using the code provided by the authors in https://github.com/rakshitha123/TSForecasting/blob/master/utils/data_loader.py. The category of each time series has been included in the dataset. This information has been obtained from the Kaggle competition page: https://www.kaggle.com/datasets/yogesh94/m4-forecasting-competition-dataset

### m4_hourly

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_hourly.parquet
+ sep:
+ index_col: timestamp
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: parquet
+ description: Time series with hourly frequency from the M4 competition. Timestamps are artificial (the M4 series have no real dates): every series starts at 12:00, and they span 2009 to 2017. Long format: one row per series and timestamp.
+ source: Monash Time Series Forecasting Repository (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks. Raw data, available in .tsf format, has been converted to Pandas format using the code provided by the authors in https://github.com/rakshitha123/TSForecasting/blob/master/utils/data_loader.py. The category of each time series has been included in the dataset. This information has been obtained from the Kaggle competition page: https://www.kaggle.com/datasets/yogesh94/m4-forecasting-competition-dataset

### ashrae_daily

+ url: https://huggingface.co/datasets/skforecast/ashrae_daily/resolve/main/ashrae_daily.parquet
+ sep:
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily energy consumption data from the ASHRAE competition with building metadata and weather data. Long format: one row per building and date.
+ source: Kaggle competition Addison Howard, Chris Balbach, Clayton Miller, Jeff Haberl, Krishnan Gowri, Sohier Dane. (2019). ASHRAE - Great Energy Predictor III. Kaggle. https://www.kaggle.com/c/ashrae-energy-prediction/overview

### bdg2_daily

+ url: https://huggingface.co/datasets/skforecast/bdg2_daily/resolve/main/bdg2_daily.parquet
+ sep:
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily energy consumption data from the Building Data Genome Project 2 with building metadata and weather data. Long format: one row per building and date. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x

### bdg2_daily_sample

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bdg2_daily_sample.csv
+ sep: ','
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Daily energy consumption data of two buildings sampled from the Building Data Genome Project 2. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x

### bdg2_hourly

+ url: https://huggingface.co/datasets/skforecast/bdg2_hourly/resolve/main/bdg2_hourly.parquet
+ sep:
+ index_col: timestamp
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: parquet
+ description: Hourly energy consumption data from the Building Data Genome Project 2 with building metadata and weather data. Long format: one row per building and timestamp. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x

### bdg2_hourly_sample

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bdg2_hourly_sample.csv
+ sep: ','
+ index_col: timestamp
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly energy consumption data of two buildings sampled from the Building Data Genome Project 2. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x

### m5

+ url: https://huggingface.co/datasets/skforecast/m5_daily/resolve/main/m5_daily.parquet
+ sep:
+ index_col: datetime
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily sales data from the M5 competition with product metadata and calendar data. Series ids keep the `_evaluation` suffix of the Kaggle files; `sell_price` is NaN before the product was first sold. Long format: one row per series and date.
+ source: Addison Howard, inversion, Spyros Makridakis, and vangelis. M5 Forecasting - Accuracy. https://kaggle.com/competitions/m5-forecasting-accuracy, 2020. Kaggle.

### ett_m1

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/ETTm1.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected from 2016-07-01 to 2018-06-26 (69,680 data points every 15 minutes). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load (LULL).
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset

### ett_m2

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/ETTm2.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected from 2016-07-01 to 2018-06-26 (69,680 data points every 15 minutes). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load (LULL).
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset

### ett_m2_extended

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/ETTm2_extended.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected from 2016-07-01 to 2018-06-26 (69,680 data points every 15 minutes). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load (LULL). Additional variables are created based on calendar information (year, month, week, day of the week, and hour). These variables have been encoded using the cyclical encoding technique (sin and cos transformations) to preserve the cyclical nature of the data.
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset

### expenditures_australia

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/expenditures_australia.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly expenditure on cafes, restaurants and takeaway food services in Victoria (Australia) from April 1982 up to April 2024.
+ source: Australian Bureau of Statistics. Catalogue No. 8501.0 https://www.abs.gov.au/statistics/industry/retail-and-wholesale-trade/retail-trade-australia/apr-2024/8501011.xlsx

### public_transport_madrid

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/public-transport-madrid.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Daily users of public transport in Madrid (Spain) from 2023-01-01 to 2024-12-15.
+ source: Consorcio Regional de Transportes de Madrid CRTM, CRTM Evolucion demanda diaria https://datos.crtm.es/documents/a7210254c4514a19a51b1617cfd61f75/about

### turbine_emission

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/turbine_emission.csv
+ sep: ','
+ index_col: datetime
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: The dataset contains 36733 instances of 11 sensor measures aggregated over one hour, from a gas turbine located in Turkey for the purpose of studying flue gas emissions, namely CO and NOx. Available variables include: Ambient temperature (AT), Ambient pressure (AP), Ambient humidity (AH), Air filter difference pressure (AFDP), Gas turbine exhaust pressure (GTEP), Turbine inlet temperature (TIT), Turbine after temperature (TAT), Compressor discharge pressure (CDP), Turbine energy yield (TEY), Carbon monoxide (CO), and Nitrogen oxides (NOx). Covered period from 2011-01-01 00:00:00 to 2015-03-11 12:00:00.
+ source: https://archive.ics.uci.edu/dataset/551/gas+turbine+co+and+nox+emission+data+set

### europe_electricity_load

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/europe_electricity_load.csv
+ sep: ','
+ index_col: datetime
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: h
+ file_type: csv
+ description: Hourly electricity load (MW) of Spain, Portugal, France, Italy and Germany from 2019-01-01 00:00 to 2025-12-31 22:00 (UTC). Values reported every 15 minutes are averaged to hourly. One binary column per country (holiday_spain, holiday_portugal, ...) flags its national public holidays, using the local date of each country. It includes real events such as the COVID-19 lockdowns of 2020 and the Iberian blackout of 2025-04-28 (Spain has no data during the blackout).
+ source: Energy-Charts.info, Fraunhofer Institute for Solar Energy Systems ISE, licensed under CC BY 4.0 (https://api.energy-charts.info/). Public holidays from Nager.Date (https://date.nager.at).
+ build script: scripts/build_europe_electricity_load.py (needs pandas; from the root of the repository: python scripts/build_europe_electricity_load.py)

## Other files

These files of `data/` are not in the `datasets` registry of skforecast, so `fetch_dataset` does not load them. Read them with `pandas.read_csv` from `https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/<file>`. Do not delete or rename them: the skforecast documentation and other tutorials link to them.

+ `bitcoin.csv`: daily Bitcoin prices (open, high, low and close), volume and market capitalization, from 2013-04-28 to 2022-01-01.
+ `demo_multi_series.csv`: five daily series (`id_1000` to `id_1004`) of different lengths in 2016, one of them with gaps. Long format: `series_id`, `timestamp`, `value`. Used in the skforecast documentation.
+ `demo_multi_series_exog.csv`: exogenous variables of `demo_multi_series.csv` for the whole of 2016 (day of the week as sine and cosine, air temperature and wind speed). Long format. Used in the skforecast documentation.
+ `energy_production_shutdown.csv`: daily energy production of a power plant from 2012-01-01 to 2014-12-30, with a shutdown from 2012-06-01 to 2012-09-30. Used in the skforecast documentation.
+ `generacion_energia_US_source.csv`: hourly electricity generation in the United States by energy source (coal, hydro, natural gas, nuclear, petroleum, solar, wind and other), from 2018-07-01 to 2021-03-15 (UTC). Long format: `date_time`, `series`, `source`.
+ `intermittent_demand.csv`: hourly series with intermittent demand (58% of the hours are zero), from 2011-01-01 to 2012-12-31.
+ `visitas_por_dia_web_cienciadedatos_2020_2021.csv`: daily users of cienciadedatos.net from 2020-07-01 to 2021-12-04, an extension of `website_visits`. Dates in `%d/%m/%y` format.

## Licenses

The BSD 3-Clause license of this repository covers its scripts and this README, not the datasets. Each dataset keeps the license or terms of use of its original source, linked in its `source`: check them before reusing it. For example, the data of the Building Data Genome Project 2 (`bdg2_*`) is under a Creative Commons Attribution-ShareAlike license (https://github.com/buds-lab/building-data-genome-project-2), and `europe_electricity_load` under CC BY 4.0.

## Changing the data

Every version of skforecast reads the files from the `main` branch of this repository, so a change in `data/` reaches all its users at once. Before merging it:

+ Run the regression test of skforecast, from the root of the skforecast repository. It downloads every dataset hosted here and checks how `fetch_dataset` reads it: `SKFORECAST_TEST_DATASETS=1 pytest skforecast/datasets/tests/tests_datasets/test_fetch_dataset_all_datasets.py -q`
+ Keep this README, the `datasets` registry of skforecast (`skforecast/datasets/datasets.py`) and the expected shapes of that test (`EXPECTED_DATASETS`) in agreement.
+ Do not rename a file, reorder its columns or change its date format: older versions of skforecast read the same file. Publish a new file instead.
