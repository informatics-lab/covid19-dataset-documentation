# Air Quality Data

## Model overview

The Met Office uses a configuration of the Unified Model (UM) to produce air quality forecasts, known as AQUM - Air Quality in the Unified Model. It is a limited area configuration, covering the UK and some of nearby European countries, on a 0.11 degree (~12km) grid. It uses UKCA with the Regional Air Quality (RAQ) chemistry mechanism, and the CLASSIC aerosol scheme.

The model is initialised at 18Z daily, to produce a 126-hour forecast: midnight-to-midnight on the next 5 days. Initial meteorological conditions are taken from the T+6 dump of the 12Z global model run, and initial chemistry and aerosol conditions are taken from T+24 of the previous AQUM run. Lateral boundary conditions are taken from the Copernicus Atmosphere Monitoring Service (CAMS) C-IFS model at ECMWF. It also makes use of GFAS emissions from ECMWF.

Operational forecasts also include a post-processing step. This concerns only the five main pollutants used by the Daily Air Quality Index (DAQI). The concentrations are regridded to a 2 km OSGB grid, a simple statistical bias correction technique based on observations is applied, and finally the DAQI is calculated.

## Daily Air Quality Index

The daily air quality index is an integer from 1-10 (inclusive) representing the overall short-term risk to health, based on a few key pollutants. These are:

- Nitrogen dioxide (NO2)
- Ozone (O3)
- Sulphur dioxide (SO2)
- Particulate matter < 2.5 micron diameter (PM2p5)
- Particulate matter < 10 micron diameter (PM10)

An index from 1-10 is derived for each of these pollutants, according to whether certain thresholds are exceeded during the given 24 hour period. Different aggregation methods are used depending on the pollutant:

- PM (both 10 and 2.5): 24h mean.
- NO2: maximum of all 1-hour means.
- SO2: maximum of all 15-minute means.
- Ozone: maximum of all 8-hr rolling means. For clarity, there are 24 such means: the first uses the first hour of the day in question and the last 7 hours of the previous day, and the 24th uses the final 8 hours of the day.

The daily air quality index is then the maximum of these individual indices. Indices 1-3 are considered "Low", 4-6 "Moderate", 7-9 "High", and 10 "Very High".

For further details, including the threshold values, see [Defra's report][daqi].

## Data

The resulting data archived to MASS includes both the raw model output in pp format, and post-processed data in nimrod format. On this platform, we expose only the post-processed data, converted to netCDF for convenience.

Mass concentrations of pollutants are given as hourly means. These are concentrations at surface level; there is no vertical component. A representative timestamp is chosen to be the end of the hour. All units are µg/m^3.

The daily air quality index is given for each day, with a representative timestamp of 12Z. The individual pollutant indices that contributed to the DAQI are not retained. Note that in order to maintain a consistent naming convention between all daily datasets, an aggregation method of "mean" is used for the purposes of naming the file (eg `aqum_daily_daqi_mean_yyyymmdd.nc`), although this is an arbitrary choice as it is not (directly) derived from hourly data at all.

Each file contains some additional attributes:

- `field_code`: code used internally to identify this variable.
- `short_name`: field code mapped to a user-friendly name (one of: DAQI, NO2, O3, SO2, PM10, PM2p5).
- `data_type`: the string "sppo", meaning Statistical Post-Processing of Observations, as opposed to "raw".


[daqi]: https://uk-air.defra.gov.uk/assets/documents/reports/cat14/1304251155_Update_on_Implementation_of_the_DAQI_April_2013_Final.pdf
