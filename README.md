
[![Build Status](https://travis-ci.com/informatics-lab/covid19-dataset-documentation.svg?branch=master)](https://travis-ci.com/informatics-lab/covid19-dataset-documentation)


# Documentation for the Met Office COVID-19 response datasets

[For more information about the data release see our blog post](https://medium.com/informatics-lab/met-office-and-partners-offer-data-and-platform-for-covid-19-researchers-83848ac55f5f).



## Auto build pipe line

### Setup and run locally:

```bash
python3 -m venv .env
. .env/bin/activate
pip install -r scripts/requirements.txt
```

#### Dry run

```bash
export SIGNED_URL="<full SAS url to blob store can be read only>"
python3 build_readme_and_index_html.py
```



#### Deploy to the blob container

```bash
export SIGNED_URL="<full SAS url to blob store read and write>"
python3 build_readme_and_index_html.py --deploy
```

### On Travis CI

Ensure that the variable `SIGNED_URL` has been configured/set on the build. It needs to be a full Shared Access Signature url to the blob container. It needs full CRUD access.

The build should only deploy the assets to the blob container on push to `master`.