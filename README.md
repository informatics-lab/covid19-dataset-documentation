## Set up:

```bash
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt
```

## Run

### Dry run

```bash
export SIGNED_URL="<full SAS url to blob store can be read only>"
python3 build_readme_and_index_html.py
```



### Deploy to the blob

```bash
export SIGNED_URL="<full SAS url to blob store read and write>"
python3 build_readme_and_index_html.py --deploy
```

.