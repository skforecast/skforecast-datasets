# skforecast-datasets

This repository contains datasets used in the skforecast library. It also contains datasets used in related tutorials.

All datasets included have a sort description as well as the original source. They can be downloaded directly from the repository or by using the `fetch_dataset()` function from the skforecast library.

```python
from skforecast.datasets import fetch_dataset()
data = fetch_dataset(name="h20")
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
+ source: Hyndman R (2023). fpp3: Data for "Forecasting: Principles and Practice" (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.

### h2o_exog

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/h2o_exog.csv
+ sep: ','
+ index_col: fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly expenditure ($AUD) on corticosteroid drugs that the Australian health system had between 1991 and 2008. Two additional variables (exog_1, exog_2) are simulated.
+ source: Hyndman R (2023). fpp3: Data for "Forecasting: Principles and Practice" (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.


### fuel_consumption

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/consumos-combustibles-mensual.csv
+ sep: ','
+ index_col: Fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly fuel consumption (tons) in Spain from 1969-01-01 to 2022-08-01.
+ source: Obtained from Corporación de Reservas Estratégicas de Productos Petrolíferos y Corporación de Derecho Público tutelada por el Ministerio para la Transición Ecológica y el Reto Demográfico. https://www.cores.es/es/estadisticas

### items_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/simulated_items_sales.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Simulated time series for the sales of 3 different items.
+ source: Simulated data

### air_quality_valencia

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/air_quality_valencia.csv
+ sep: ','
+ index_col: datetime
+ date_format: date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: csv
+ description: Hourly measures of several air chemical pollutant at Valencia city (Avd. Francia) from 2019-01-01 to 20213-12-31. Including the following variables: pm2.5 (µg/m³), CO (mg/m³), NO (µg/m³), NO2 (µg/m³), PM10 (µg/m³), NOx (µg/m³), O3 (µg/m³), Veloc. (m/s), Direc. (degrees), SO2 (µg/m³)
+ source: Red de Vigilancia y Control de la Contaminación Atmosférica, 46250047-València - Avd. Francia, https://mediambient.gva.es/es/web/calidad-ambiental/datos-historicos

### air_quality_valencia_no_missing

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/air_quality_valencia_no_missing.csv
+ sep: ','
+ index_col: datetime
+ date_format: date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: csv
+ description: Hourly measures of several air chemical pollutant (pm2.5, co, no, no2, pm10, nox, o3, veloc. (air speed), direc. (air direction), so2) at Valencia city. Units are (µg/m3) for pm2.5, no, no2, pm10, so2, (mg/m3) for co, (m/s) for veloc. and (degrees) for direc. Missing values have been removed using linear interpolation. Missing values have been imputed using linear interpolation.
+ source: Red de Vigilancia y Control de la Contaminación Atmosférica, 46250047-València - Avd. Francia, https://mediambient.gva.es/es/web/calidad-ambiental/datos-historicos

### website_visits

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/visitas_por_dia_web_cienciadedatos.csv
+ sep: ","
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Daily visits to the cienciadedatos.net website registered with the google analytics service.
+ source: Amat Rodrigo, J. (2021). cienciadedatos.net (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.10006330

### bike_sharing

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_dataset_clean.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: csv
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### bike_sharing_extended_features

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_extended_features.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: csv
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling. Additionally, the dataset was enriched by introducing supplementary features. Additions include calendar-based variables (day of the week, hour of the day, month, etc.), indicators for sunlight, rolling temperature averages, and polynomial features generated from variable pairs. All cyclic variables are encoded using sine and cosine transformations.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### australia_tourism

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/australia_tourism.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d
+ freq: Q
+ file_type: csv
+ description: Quarterly overnight trips (in thousands) from 1998 Q1 to 2016 Q4 across Australia. The tourism regions are formed through the aggregation of Statistical Local Areas (SLAs) which are defined by the various State and Territory tourism authorities according to their research and marketing needs. 
+ source: Wang, E, D Cook, and RJ Hyndman (2020). A new tidy data structure to support exploration and modeling of temporal data, Journal of Computational and Graphical Statistics, 29:3, 466-478, doi:10.1080/10618600.2019.1695624.

### uk_daily_flights

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/uk_daily_flights.csv
+ sep: ','
+ index_col: Date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: Daily number of flights in UK from 02/01/2019 to 23/01/2022.
+ source: Experimental statistics published as part of the Economic activity and social change in the UK, real-time indicators release, Published 27 January 2022. Daily flight numbers are available in the dashboard provided by the European Organisation for the Safety of Air Navigation (EUROCONTROL). https://www.ons.gov.uk/economy/economicoutputandproductivity/output/bulletins/economicactivityandsocialchangeintheukrealtimeindicators/latest

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
+ description: Half-hourly electricity demand for Victoria, Australia
+ source: O'Hara-Wild M, Hyndman R, Wang E, Godahewa R (2022).tsibbledata: Diverse Datasets for 'tsibble'. https://tsibbledata.tidyverts.org/, https://github.com/tidyverts/tsibbledata/. https://tsibbledata.tidyverts.org/reference/vic_elec.html

### store_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/store_sales.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: This dataset contains 913,000 sales transactions from 2013-01-01 to 2017-12-31 for 50 products (SKU) in 10 stores.
+ source: inversion. (2018). Store Item Demand Forecasting Challenge. Kaggle. https://kaggle.com/competitions/demand-forecasting-kernels-only

### bicimad

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bicimad_users.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: This dataset contains the daily users of the bicycle rental service (BiciMad) in the city of Madrid (Spain) from 2014-06-23 to 2022-09-30.
+ source: Portal de datos abiertos del Ayuntamiento de Madrid https://datos.madrid.es/portal/site/egob'

### m4_daily

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_daily.parquet
+ sep: 
+ index_col: start_timestamp
+ timestamp: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: parquet
+ description: Time series with daily frequency from the M4 competition.
+ source: Monash Time Series Forecasting Repository  (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks.

### m4_hourly

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_hourly.parquet
+ sep: 
+ index_col: start_timestamp
+ timestamp: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: parquet
+ description: Time series with hourly frequency from the M4 competition.
+ source: Monash Time Series Forecasting Repository  (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks.

### ashrae_daily

+ url: https://drive.google.com/file/d/1fMsYjfhrFLmeFjKG3jenXjDa5s984ThC/view?usp=sharing
+ sep: 
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily energy consumption data from the ASHRAE competition with building metadata and weather data.
+ source: Kaggle competition Addison Howard, Chris Balbach, Clayton Miller, Jeff Haberl, Krishnan Gowri, Sohier Dane. (2019). ASHRAE - Great Energy Predictor III. Kaggle. https://www.kaggle.com/c/ashrae-energy-prediction/overview

### bdg2_daily

+ url: https://drive.google.com/file/d/1KHYopzclKvS1F6Gt6GoJWKnxiuZ2aqen/view?usp=sharing
+ sep: 
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily energy consumption data from the The Building Data Genome Project 2 with building metadata and weather data. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x

### bdg2_hourly

+ url: https://drive.google.com/file/d/1I2i5mZJ82Cl_SHPTaWJmLoaXnntdCgh7/view?usp=sharing
+ sep: 
+ index_col: timestamp
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ file_type: parquet
+ description: Hourly energy consumption data from the The Building Data Genome Project 2 with building metadata and weather data. https://github.com/buds-lab/building-data-genome-project-2
+ source: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition. Sci Data 7, 368 (2020). https://doi.org/10.1038/s41597-020-00712-x


### m5

+ url: (4 partitions)
    + https://drive.google.com/file/d/1JOqBsSHegly6iSJFgmkugAko734c6ZW5/view?usp=sharing
    + https://drive.google.com/file/d/1BhO1BUvs-d7ipXrm7caC3Wd_d0C_6PZ8/view?usp=sharing
    + https://drive.google.com/file/d/1oHwkQ_QycJVTZMb6bH8C2klQB971gXXA/view?usp=sharing
    + https://drive.google.com/file/d/1OvYzFlDG04YgTvju2k02vHEOj0nIuwei/view?usp=sharing
+ sep: 
+ index_col: timestamp
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: parquet
+ description: Daily sales data from the M5 competition with product metadata and calendar data.
+ source: Addison Howard, inversion, Spyros Makridakis, and vangelis. M5 Forecasting - Accuracy. https://kaggle.com/competitions/m5-forecasting-accuracy, 2020. Kaggle.


### ett_m1

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/refs/heads/main/data/ETTm1.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected between July 2016 and July 2018 (2 years × 365 days × 24 hours × 4 intervals per hour = 70,080 data points). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load(LULL).
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset


### ett_m2

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/ETTm2.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected between July 2016 and July 2018 (2 years × 365 days × 24 hours × 4 intervals per hour = 70,080 data points). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load(LULL).
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset


### ett_m2_extended

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/ETTm2_extended.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: 15min
+ file_type: csv
+ description: Data from an electricity transformer station was collected between July 2016 and July 2018 (2 years × 365 days × 24 hours × 4 intervals per hour = 70,080 data points). Each data point consists of 8 features, including the date of the point, the predictive value "Oil Temperature (OT)", and 6 different types of external power load features: High UseFul Load (HUFL), High UseLess Load (HULL), Middle UseFul Load (MUFL), Middle UseLess Load (MULL), Low UseFul Load (LUFL), Low UseLess Load(LULL). Additional variables are created based on calendar information (year, month, week, day of the week, and hour). These variables have been encoded using the cyclical encoding technique (sin and cos transformations) to preserve the cyclical nature of the data.
+ source: Zhou, Haoyi & Zhang, Shanghang & Peng, Jieqi & Zhang, Shuai & Li, Jianxin & Xiong, Hui & Zhang, Wancai. (2020). Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting. [10.48550/arXiv.2012.07436](https://arxiv.org/abs/2012.07436). https://github.com/zhouhaoyi/ETDataset


### expenditures_australia

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/refs/heads/main/data/expenditures_australia.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: MS
+ file_type: csv
+ description: Monthly expenditure on cafes, restaurants and takeaway food services in Victoria (Australia) from April 1982 up to April 2024.
+ source: Australian Bureau of Statistics. Catalogue No. 8501.0 https://www.abs.gov.au/statistics/industry/retail-and-wholesale-trade/retail-trade-australia/apr-2024/8501011.xlsx


### public_transport_madrid

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/refs/heads/main/data/public-transport-madrid.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ file_type: csv
+ description: daily user of public transport in Madrid (Spain) from 2023-01-01 to 2024-12-15.
+ source: Consorcio Regional de Transportes de Madrid CRTM, CRTM Evolucion demanda diaria https://datos.crtm.es/documents/a7210254c4514a19a51b1617cfd61f75/about