# Data available on Met Office Informatics Lab COVID-19 response platform

This data is for COVID-19 researchers to explore relationships between COVID-19 and environmental factors. [For more information see our blog post](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f).


## Updates
Check here for regular updates on the data, such as the provision of new datasets.

#### Update 14 April 2020
- Due to constant data updates, we have organised the `/data/covid19-ancillary-data/` directory to have a `latest/` folder where you will find the most up-to-date datasets.
Data from previous iterations will still be available; <br>e.g. `/data/covid19-ancillary-data/10-04-20T22.05.00`<br>
There are no guarantees that older versions of the data will be made available indefinitely, so please use `latest/` where possible.
- UKV meteorological datasets are now available in `mo_data_ukv_daily/` and `mo_data_ukv_hourly/`. These datasets are from the [UKV](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/weather-forecasting) numerical weather prediction model, a Met Office UK regional model, for 01 Jan - 12 Apr 2020 (inclusive).


## Quick links.

#### - [Announcement by the Met Office](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-compute-platform-for-covid-19-researchers-83848ac55f5f) making this data available in response to [RAMP](https://epcced.github.io/ramp/) initiatie, asking for assistance in tackling to the COVID-19 pandemic.

#### - You can browse the data we have made available on Azure [here](index.html).

#### - This data is made available under [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

#### - More data is coming! Please subscribe to our [Google Groups mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join) to receive updates when that data is available.

#### - Please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk) if you have any questions.



## Quick start.

### What data is available?
The Met Office have made available global meteorological data with the following variables:

- `t1o5m` = Air temperature at 1.5m in $K$
- `sh` = Specific humidity at 1.5m in $kg/kg$ (kg of water vapor in kg of air)
- `sw` = Short wave radiation in $W m^{-2}$ (surrogate for sunshine)
- `precip` = Precipitation flux in $kg m^{-2} s^{-1}$ (multiply by 3600 to get $mm / hr$)
- `pmsl` = Air pressure at mean sea level in $Pa$

This data is available in a gridded data format as NetCDF files (`.nc`).

We have also processed the data into regional daily values for all reporting regions in the UK and state counties in the USA. This data is available as Comma Seperate Variable files (`.csv`).

The data is stored on Azure Blob Storage, which can be either simply downloaded to your choice of computer or accessed through the [Met Office Informatics Lab COVID-19 response platform](https://covid19-response.informaticslab.co.uk/).

### Downloading Data
The data is hosted on Microsoft Azure through their AI for Earth initiative. You can download the data in two ways:

#### Method one: point and click
Open [this link](https://metdatasa.blob.core.windows.net/covid19-response/index.html) in your browser. You will see a list of links to datafiles which you can download by clicking on them in your browser.

#### Method two: automated downloading with AZCopy
There are lots of files, so we suggest installing `azcopy` command line tool, which you can download [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy). This lets you download [whole directories](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#download-the-contents-of-a-directory) or multiple files [using wildcards](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#use-wildcard-characters-1) to your computer of choice. <br>
For example: <br>
1. `azcopy cp https://metdatasa.blob.core.windows.net/covid19-response/latest/mo_data_global_daily/precip_max/precip_day_max_20200101.nc my_directory/`<br>
will download the file `precip_day_max_20200101.nc` to `my_directory/`.
2. `azcopy cp https://metdatasa.blob.core.windows.net/covid19-response/latest/mo_data_global_daily/sh_mean/* my_directory/`<br>
will download the contents of `/mo_data_global_daily/sh_mean/` to `my_directory/`.
3. `azcopy cp https://metdatasa.blob.core.windows.net/covid19-response/latest/regional_subset_data/us_data/ --include-pattern us_55*.csv`<br>
will download all the US state county averaged meteorology data which match the pattern `us_55*.csv`.


### How is the data organised on this platform?
All this data is available in the `/data/covid19-ancillary-data/latest/` directory. 
The `datasets/` symlink on your user homespace directs you to it. <br>
Here is a guide to the folder structure:

- `/data/covid19-ancillary-data/latest/mo_data_global_daily/`<br>
Contains the Met Office daily global gridded data files for 01 Jan - 31 Mar 2020.<br>
Each file has a descriptive name* as `{variable}_{statistic}_{YYYYMMDD}.nc`.
    - `.../t1o5m_mean/` = Daily mean air temperature files
    - `.../t1o5m_max/` = Daily max air temperature files
    - `.../t1o5m_min/` = Daily min air temperature files
    - `.../sh_mean/` = Daily mean Specific Humidity files
    - `.../sh_max/` = Daily max Specific Humidity files
    - `.../sh_min/` = Daily min Specific Humidity files
    - `.../sw_mean/` = Daily mean for short wave radiation files
    - `.../sw_max/` = Daily max for short wave radiation files
    - `.../precip_mean/` = Daily mean precipitation flux files
    - `.../precip_max/` = Daily max precipitation flux files
    
    
- `/data/covid19-ancillary-data/latest/mo_data_global_hourly/`<br>
Contains the Met Office hourly global gridded data files for 01 Jan - 31 Mar 2020.<br>
Each file has a descriptive name* as `{variable}_global_{YYYYMMDD}.nc`.
    - `.../t1o5m/` = Hourly air temperature files
    - `.../sh/` = Hourly Specific Humidity files
    - `.../sw/` = Hourly for short wave radiation files
    - `.../precip/` = Hourly precipitation flux files
    - `.../precip3hr/` = Three hourly precipitation flux files
    - `.../pmsl/` = Hourly air pressure at mean sea level files


- `/data/covid19-ancillary-data/latest/regional_subset_data/`<br>
Contains processed regional daily values for UK and USA as `.csv` files for 01 Jan - 31 Mar 2020.<br>
Files were processed by subsetting the gridded Met Office global daily files using shapefiles for each region, taking the latitude-longitude mean value for each variable in each region for each date and saving those values as a table in a `.csv` file*.
    - `.../uk_daily_meteodata_2020jan-mar_v03.csv` <br>
    Daily values for `t1o5m`, `sh`, `sw` and `precip` for **all** reporting regions in the UK. <br>
    (Merging together of all files in `/uk_data/` and `/uk_data_precip`)
    - `.../us_daily_meteodata_2020jan-mar_v03.csv`<br>
    Daily values for `t1o5m`, `sh`, `sw` and `precip` for **all** counties in the USA. <br>
    (Merging together of all files in `/us_data/` and `/us_data_precip`)
    - `.../uk_data/`<br> 
    Daily values for `t1o5m`, `sh` and `sw` for **each** reporting region in the UK. (One `.csv` file per region.)
    - `.../uk_data_precip/`<br> 
    Daily values for `precip` for **each** reporting region in the UK. (One `.csv` file per region.)
    - `.../us_data/`<br>
    Daily values for `t1o5m`, `sh` and `sw` for **each** county in the USA. (One `.csv` file per county.)
    - `.../us_data_precip/`<br>
    Daily values for `precip` for **each** county in the USA. (One `.csv` file per county.)


- `/data/covid19-ancillary-data/latest/shapefiles/`<br>
Contains shapefiles for UK, USA, Italy, Uganda and Vietnam.
    - `.../UK/` = UK COVID-19 reporting regions
    - `.../USA/` = USA state counties 
    - `.../Italy/` = 
    - `.../Uganda/` = 
    - `.../Vietnam/` = 


- `/data/covid19-ancillary-data/latest/mo_data_ukv_daily/`<br>
Contains the Met Office daily UKV gridded data files for 01 Jan - 12 Apr 2020 (inclusive).<br>
Each file has a descriptive name* as `{variable}_ukv_{YYYYMMDD}.nc`.
    - `.../t1o5m_mean/` = Daily mean air temperature files
    - `.../t1o5m_max/` = Daily max air temperature files
    - `.../t1o5m_min/` = Daily min air temperature files
    - `.../sh_mean/` = Daily mean Specific Humidity files
    - `.../sh_max/` = Daily max Specific Humidity files
    - `.../sh_min/` = Daily min Specific Humidity files
    - `.../sw_mean/` = Daily mean for short wave radiation files
    - `.../sw_max/` = Daily max for short wave radiation files    


- `/data/covid19-ancillary-data/latest/mo_data_ukv_hourly/`<br>
Contains the Met Office hourly UKV gridded data files for 01 Jan - 12 Apr 2020 (inclusive).<br>
Each file has a descriptive name* as `{variable}_ukv_{YYYYMMDD}.nc`.
    - `.../t1o5m_ukv/` = Hourly air temperature files
    - `.../sh_ukv/` = Hourly Specific Humidity files
    - `.../sw_ukv/` = Hourly for short wave radiation files
    - `.../pmsl_ukv/` = Hourly air pressure at mean sea level files
    
__*Where possible, filenames are as described. However, given the short timeframes in which this data has been made available, minor variations in filename descriptions may occur. Filenames should still be accurately descriptive of the data. If you find issues with any filenames, or the data itself, please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk)__