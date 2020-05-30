# Met Office COVID-19 response dataset

This data is for COVID-19 researchers to explore relationships between COVID-19 and environmental factors. [For more information see our blog post](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f). If your require compute resources to process this data [we might be able to help](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f).

## License

_Users are required to acknowledge the Met Office as the source of these data by including the following attribution statement in any resulting products, publications or applications: <br>"Contains Met Office data licensed under the Open Government Licence v3.0"_

This data is made available under [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## About the data

Global and high resolution UK [numerical weather model output](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/weather-forecasting) from the [UK Met Office](https://www.metoffice.gov.uk/). Data is from the very early time steps of the model following data assimilation, as such this data approximates a whole earth observation dataset.

The following variables are available:

- `t1o5m` = Air temperature at 1.5m in _**K**_
- `sh` = Specific humidity at 1.5m in _**kg/kg**_ (kg of water vapor in kg of air)
- `sw` = Short wave radiation in _**W m<sup>-2</sup>**_ (surrogate for sunshine)
- `precip` = Precipitation flux in _**kg m<sup>-2</sup> s<sup>-1</sup>**_ (multiply by 3600 to get _**mm / hr**_)
- `snow` = Stratiform snowfall flux in _**kg m<sup>-2</sup> s<sup>-1</sup>**_ (multiply by 3600 to get _**mm / hr**_)
- `rain` = Stratiform rainfall flux in _**kg m<sup>-2</sup> s<sup>-1</sup>**_ (multiply by 3600 to get _**mm / hr**_)
- `pmsl` = Air pressure at mean sea level in _**Pa**_
- `windspeed` = Wind speed in _**m s<sup>-1</sup>**_
- `windgust` = Wind gust in _**m s<sup>-1</sup>**_
- `cldbase` = Cloud base altitude in _**ft**_
- `cldfrac` = Cloud area fraction assuming maximum random overlap (_**unitless: 0-1**_)

Output of the Met Office UK air quality model AQUM is also available. This includes the following variables:

- `daqi` = Daily Air Quality Index, an integer from _**1-10**_
- `no2` = Nitrogen dioxide concentration, in _**µg m<sup>-3</sup>**_
- `o3` = Ozone concentration, in _**µg m<sup>-3</sup>**_
- `so2` = Sulphur dioxide concentration, in _**µg m<sup>-3</sup>**_
- `pm2p5` = Concentration of particulate matter less than 2.5 microns diameter, in _**µg m<sup>-3</sup>**_
- `pm10` = Concentration of particulate matter less than 10 microns diameter, in _**µg m<sup>-3</sup>**_

Output of the Met Office UK air quality model AQUM is also available. This includes the following variables:

- `daqi` = Daily Air Quality Index, an integer from 1-10
- `no2` = Nitrogen dioxide concentration, in _**µg m<sup>-3</sup>**_
- `o3` = Ozone concentration, in _**µg m<sup>-3</sup>**_
- `so2` = Sulphur dioxide concentration, in _**µg m<sup>-3</sup>**_
- `pm2p5` = Concentration of particulate matter less than 2.5 microns diameter, in _**µg m<sup>-3</sup>**_
- `pm10` = Concentration of particulate matter less than 10 microns diameter, in _**µg m<sup>-3</sup>**_

This data is made available as NetCDF files.

Global and UK model data updated is available from 01 Jan 2020 onwards. The dataset is updated daily for the previous day.

For detailed information about how this data is generated and the particulars of the parameters please see the technical references:

- [Meteorology](https://metdatasa.blob.core.windows.net/covid19-response/README_data_processing.pdf).
- [Air Quality](https://metdatasa.blob.core.windows.net/covid19-response/README_data_air_quality.html).

There is some additional post processed data aggregations over COVID-19 reporting regions in the UK and USA made available as CSV files. More details below.

## Quick links

- [Announcement by the Met Office](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-compute-platform-for-covid-19-researchers-83848ac55f5f) making this data available in response to [RAMP](https://epcced.github.io/ramp/) initiative, asking for assistance in tackling to the COVID-19 pandemic.

- You can browse the data we have made available on Azure [here](index.html).

- This data is made available under [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

- More data is coming! Please subscribe to our [Google Groups mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join) to receive updates when that data is available.

- Please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk) if you have any questions or requests for additional data.

## Data volumes, retention, update frequency and location

The gridded data is updated daily for the previous day.

The CSV data is updated on request (when possible), contact [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk) if you have a need for this data to be avaliable more frequently.

As of 18/04/20 the dataset totals approximately 352G.

It grows weekly by approximately 22G a week.

We intend retain and make this data available as long as we believe it's useful in planing the response to the COVID-19 pandemic.

The data is stored in the Azure region `East US 2`.

## Quick start

### Accessing the data

The data is hosted on Microsoft Azure through their AI for Earth initiative. You can access the data in many ways, such as:

#### Point and click

Open [the index file](https://metdatasa.blob.core.windows.net/covid19-response/index.html) in your browser. You will see a list of links to datafiles which you can download by clicking on them in your browser.

#### Azure Blob libraries

There is a range of libraries in a range of languages for working with Azure Blobs. See the [Azure Blob documentation for more info](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview).

#### Automated downloading with AZCopy

There are lots of files, so we suggest installing `azcopy` command line tool, which you can download [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy). This lets you download [whole directories](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#download-the-contents-of-a-directory) or multiple files [using wildcards](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#use-wildcard-characters-1) to your computer of choice. <br>

For example: <br>
1. Download the file `global_daily_precip_max_20200101.nc` to the current directory:

```azcopy cp "https://metdatasa.blob.core.windows.net/covid19-response/metoffice_global_daily/precip_max/global_daily_precip_max_20200101.nc" .```

2. Download the contents of `/metoffice_ukv_daily/snow_mean/` to `ukv_daily_snow_mean/`:

```azcopy cp "https://metdatasa.blob.core.windows.net/covid19-response/metoffice_ukv_daily/snow_mean/*" ukv_daily_snow_mean/```

3. Download all the US state county averaged meteorology data which match the pattern `us_55*.csv`:

```azcopy cp "https://metdatasa.blob.core.windows.net/covid19-response/regional_subset_data/us_data/" . --recursive  --include-pattern "us_55*.csv"```

## How the data is organised

- `metoffice_global_daily/`<br>
Contains the Met Office daily global gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `global_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

- `metoffice_global_hourly/`<br>
Contains the Met Office hourly global gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `global_hourly_{variable}_{YYYYMMDD}.nc`.

- `metoffice_ukv_daily/`<br>
Contains the Met Office daily UKV gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `ukv_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

- `metoffice_ukv_hourly/`<br>
Contains the Met Office hourly UKV gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `ukv_hourly_{variable}_{YYYYMMDD}.nc`.

- `metoffice_aqum_daily/`<br>
Contains the Met Office daily AQUM gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `aqum_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

- `metoffice_aqum_hourly/`<br>
Contains the Met Office hourly AQUM gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `aqum_hourly_{variable}_{YYYYMMDD}.nc`.

- `regional_subset_data/`<br>
Contains processed regional daily values for UK, USA, Italy, Brazil, Vietnam and Uganda as `.csv` files.<br>
Processed for data 01 Jan - 19 Apr 2020, including all variables except `wind_speed` and `wind_gust`.
Files were processed by subsetting the gridded Met Office global daily files using shapefiles for each region, taking the latitude-longitude mean and variance values for each variable in each region for each date, and saving those values as a table in a `.csv` file*.
Each file in this directory has a descriptive name* as `{shapefile_name}_metoffice_global_daily_{start_date}-{end_date}.csv`.

- `shapefiles/`<br>
Contains shapefiles for UK, USA, Italy, Brazil, Uganda and Vietnam.
  - `.../UK/` = UK COVID-19 reporting regions
  - `.../USA/` = USA state counties
  - `.../Italy/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Italy
  - `.../Brazil/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Brazil
  - `.../Uganda/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Uganda
  - `.../Vietnam/` = [GADM v3.6](https://gadm.org/download_country_v3.html) administrative level 2 for Vietnam

_*Where possible, filenames are as described. However, given the short timeframes in which this data has been made available, minor variations in filename descriptions may occur. Filenames should still be accurately descriptive of the data. If you find issues with any filenames, or the data itself, please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk)_

## Getting help and contact

For help or additional data requests please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk).
