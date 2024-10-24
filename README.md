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
+ description: Monthly expenditure ($AUD) on corticosteroid drugs that the Australian health system had between 1991 and 2008.
+ source: Hyndman R (2023). fpp3: Data for "Forecasting: Principles and Practice" (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.

### h2o_exog

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/h2o_exog.csv
+ sep: ','
+ index_col: fecha
+ date_format: %Y-%m-%d
+ freq: MS
+ description: Monthly expenditure ($AUD) on corticosteroid drugs that the Australian health system had between 1991 and 2008. Two additional variables (exog_1, exog_2) are simulated.
+ source: Hyndman R (2023). fpp3: Data for "Forecasting: Principles and Practice" (3rd Edition). http://pkg.robjhyndman.com/fpp3package/, https://github.com/robjhyndman/fpp3package, http://OTexts.com/fpp3.


### fuel_consumption

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/consumos-combustibles-mensual.csv
+ sep: ','
+ index_col: Fecha
+ date_format: %Y-%m-%d
+ freq: MS,
+ description: Monthly fuel consumption (tons) in Spain from 1969-01-01 to 2022-08-01.
+ source: Obtained from Corporación de Reservas Estratégicas de Productos Petrolíferos y Corporación de Derecho Público tutelada por el Ministerio para la Transición Ecológica y el Reto Demográfico. https://www.cores.es/es/estadisticas

### items_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/simulated_items_sales.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ description: Simulated time series for the sales of 3 different items.
+ source: Simulated data

### air_quality_valencia

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/air_quality_valencia.csv
+ sep: ','
+ index_col: datetime
+ date_format: date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ description: Hourly measures of several air quimical pollutant (pm2.5, co, no, no2, pm10, nox, o3, so2) at Valencia city.
+ source: Red de Vigilancia y Control de la Contaminación Atmosférica, 46250054-València - Centre, https://mediambient.gva.es/es/web/calidad-ambiental/datos-historicos

### website_visits

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/visitas_por_dia_web_cienciadedatos.csv
+ sep: ","
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ description: Daily visits to the cienciadedatos.net website registered with the google analytics service.
+ source: Amat Rodrigo, J. (2021). cienciadedatos.net (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.10006330

### bike_sharing

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_dataset_clean.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### bike_sharing_extended_features

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bike_sharing_extended_features.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d %H:%M:%S
+ freq: H
+ description: Hourly usage of the bike share system in the city of Washington, D.C. during the years 2011 and 2012. In addition to the number of users per hour, information about weather conditions and holidays is available. The following modifications have been applied to the original data: Renamed columns with more descriptive names, renamed categories of the weather variables, the category of 'heavy_rain' has been combined with that of 'rain', denormalized temperature, humidity and wind variables, 'date_time' variable created and set as index, imputed missing values by forward filling. Additionally, the dataset was enriched by introducing supplementary features. Additions include calendar-based variables (day of the week, hour of the day, month, etc.), indicators for sunlight, rolling temperature averages, and polynomial features generated from variable pairs. All cyclic variables are encoded using sine and cosine transformations.
+ source: Fanaee-T,Hadi. (2013). Bike Sharing Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894.

### australia_tourism

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/australia_tourism.csv
+ sep: ','
+ index_col: date_time
+ date_format: %Y-%m-%d
+ freq: Q
+ description: Quarterly overnight trips (in thousands) from 1998 Q1 to 2016 Q4 across Australia. The tourism regions are formed through the aggregation of Statistical Local Areas (SLAs) which are defined by the various State and Territory tourism authorities according to their research and marketing needs. 
+ source: Wang, E, D Cook, and RJ Hyndman (2020). A new tidy data structure to support exploration and modeling of temporal data, Journal of Computational and Graphical Statistics, 29:3, 466-478, doi:10.1080/10618600.2019.1695624.

### uk_daily_flights

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/uk_daily_flights.csv
+ sep: ','
+ index_col: Date
+ date_format: %Y-%m-%d
+ freq: D
+ description: Daily number of flights in UK from 02/01/2019 to 23/01/2022.
+ source: Experimental statistics published as part of the Economic activity and social change in the UK, real-time indicators release, Published 27 January 2022. Daily flight numbers are available in the dashboard provided by the European Organisation for the Safety of Air Navigation (EUROCONTROL). https://www.ons.gov.uk/economy/economicoutputandproductivity/output/bulletins/economicactivityandsocialchangeintheukrealtimeindicators/latest


### wikipedia_visits

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/wikipedia_visits.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ description: Log daily page views for the Wikipedia page for Peyton Manning. Scraped data using the Wikipediatrend package in R.
+ source: https://github.com/facebook/prophet/blob/main/examples/example_wp_log_peyton_manning.csv


### vic_electricity

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/vic_electricity.csv
+ sep: ','
+ index_col: Time
+ date_format: %Y-%m-%dT%H:%M:%SZ
+ freq: 30min
+ description: Half-hourly electricity demand for Victoria, Australia
+ source: O'Hara-Wild M, Hyndman R, Wang E, Godahewa R (2022).tsibbledata: Diverse Datasets for 'tsibble'. https://tsibbledata.tidyverts.org/, https://github.com/tidyverts/tsibbledata/. https://tsibbledata.tidyverts.org/reference/vic_elec.html


### store_sales

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/store_sales.csv
+ sep: ','
+ index_col: date,
+ date_format: %Y-%m-%d
+ freq: D
+ description: This dataset contains 913,000 sales transactions from 2013-01-01 to 2017-12-31 for 50 products (SKU) in 10 stores.
+ source: inversion. (2018). Store Item Demand Forecasting Challenge. Kaggle. https://kaggle.com/competitions/demand-forecasting-kernels-only

### bicimad

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/bicimad_users.csv
+ sep: ','
+ index_col: date,
+ date_format: %Y-%m-%d
+ freq: D
+ description: This dataset contains the daily users of the bicycle rental service (BiciMad) in the city of Madrid (Spain) from 2014-06-23 to 2022-09-30.
+ source: Portal de datos abiertos del Ayuntamiento de Madrid https://datos.madrid.es/portal/site/egob'

### m4_hourly

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_hourly.parquet
+ sep: 
+ index_col: start_timestamp,
+ timestamp: %Y-%m-%d %H:%M:%S
+ freq: H
+ description: Time series with hourly frequency from the M4 competition.
+ source: Monash Time Series Forecasting Repository  (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks.

### m4_daily

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/m4_daily.parquet
+ sep: 
+ index_col: start_timestamp,
+ timestamp: %Y-%m-%d %H:%M:%S
+ freq: H
+ description: Time series with daily frequency from the M4 competition.
+ source: Monash Time Series Forecasting Repository  (https://zenodo.org/communities/forecasting) Godahewa, R., Bergmeir, C., Webb, G. I., Hyndman, R. J., & Montero-Manso, P. (2021). Monash Time Series Forecasting Archive. In Neural Information Processing Systems Track on Datasets and Benchmarks.


### air_pollution

+ url: https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/guangyuan_air_pollution.csv
+ sep: ','
+ index_col: date
+ date_format: %Y-%m-%d
+ freq: D
+ description:
+ source:
