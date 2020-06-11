# Met Office COVID-19 non-commercial response dataset

This data is for COVID-19 researchers to explore relationships between COVID-19 and environmental factors. It is offered under a non-commercial license.

## Stay up to date

Stay up to date with new datasets, corrections, redactions and useful or important information by subscribing to our [Google Groups mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join)

## License

_Users are required to acknowledge the Met Office as the source of these data by including the following attribution statement in any resulting products, publications or applications: “Contains Met Office data licensed under the Non-Commercial government license version v2.0”_

This data is made available under [Non-Commercial Government License](http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/).

## About the data

High resolution UK [numerical weather model output](https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/weather-forecasting) from the [UK Met Office](https://www.metoffice.gov.uk/). Data is from the very early time steps of the model following data assimilation, as such this data approximates a UK observation dataset.

The following variables are available:

- `t1o5m` = Air temperature at 1.5m in _**K**_
- `sh` = Specific humidity at 1.5m in _**kg/kg**_ (kg of water vapor in kg of air)
- `sw` = Short wave radiation in _**W m<sup>-2</sup>**_ (surrogate for sunshine)
- `snow` = Stratiform snowfall flux in _**kg m<sup>-2</sup> s<sup>-1</sup>**_ (multiply by 3600 to get _**mm / hr**_)
- `rain` = Stratiform rainfall flux in _**kg m<sup>-2</sup> s<sup>-1</sup>**_ (multiply by 3600 to get _**mm / hr**_)
- `pmsl` = Air pressure at mean sea level in _**Pa**_
- `windspeed` = Wind speed in _**m s<sup>-1</sup>**_
- `windgust` = Wind gust in _**m s<sup>-1</sup>**_
- `cldbase` = Cloud base altitude in _**ft**_
- `cldfrac` = Cloud area fraction assuming maximum random overlap (_**unitless**_)

This data is made available as NetCDF files.

Global and UK model data updated is available from 01/04/2015 to 2019/12/13.

## Missing data

Data for September 19th 2019 is unavailable.

## Quick links

- We keep expanding our data offering. Please subscribe to our [Google Groups mailing list](https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join) to receive updates when that data is available.

- Please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk) if you have any questions or requests for additional data.


## Quick start

### Accessing the data

The data is hosted on Microsoft Azure through their AI for Earth initiative. You can access the data in numerous ways, such as:

#### Index page

There data in this container is listed on the [index page](index.html). You can see what is avaliable and download files one at at time from this page. It is *not* recomended for accessing any significant volume of data.

#### Azure Blob libraries

There is a range of libraries in a range of languages for working with Azure Blobs. See the [Azure Blob documentation for more info](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview).

#### Automated downloading with AZCopy

There are lots of files, so we suggest installing `azcopy` command line tool, which you can download [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy). This lets you download [whole directories](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#download-the-contents-of-a-directory) or multiple files [using wildcards](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-blobs?toc=/azure/storage/blobs/toc.json#use-wildcard-characters-1) to your computer of choice. <br>


## How the data is organised

- `metoffice_ukv_daily/`<br>
Contains the Met Office daily UKV gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `ukv_daily_{variable}_{statistic}_{YYYYMMDD}.nc`.

- `metoffice_ukv_hourly/`<br>
Contains the Met Office hourly UKV gridded data files.<br>
There is a 'directory' for each variable.<br>
Each file in these directories has a descriptive name* as `ukv_hourly_{variable}_{YYYYMMDD}.nc`.


## Getting help and contact

For help or additional data requests please contact us on [covid19@informaticslab.co.uk](mailto:covid19@informaticslab.co.uk).
