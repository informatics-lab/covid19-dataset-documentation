import os
from collections import namedtuple
import datetime
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings
from markdown import markdown
from collections import namedtuple
import sys


print(f"### Args: {sys.argv}")
DRY_RUN = False if (len(sys.argv) >= 2 and sys.argv[1].strip() == '--deploy') else True
print("### DRY RUN ###" if DRY_RUN else "### DEPLOY ###")


BlobAccess = namedtuple('BlobAccess', ['account', 'container', 'credentials'])

def account_details(signed_url):
    # set up blob access
    container = signed_url.split('/')[3].split('?')[0]
    account = signed_url.split('/')[2]
    credentials = signed_url.split('?', 1)[1]

    return BlobAccess(account=account, container=container, credentials=credentials)

def blob_clients(blob_access):
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient(f"https://{blob_access.account}/?{blob_access.credentials}")
    container_client = blob_service_client.get_container_client(blob_access.container)

    return blob_service_client, container_client


def build_index(blob_access):
    blob_service_client, container_client = blob_clients(blob_access)

    print("\nListing blobs...")
    # List the blobs in the container
    blob_list = container_client.list_blobs()
    blobs = [blob.name for blob in blob_list]  # if blob.name[0] != '.' and blob.name.find('/.') == -1]
    print(f"found {len(blobs)} blobs")

    # filter out 'hidden' files
    clean_blobs = []
    for blob in blobs:
        if blob[0] == '.' or blob.find('/.') >= 0:
            continue
        clean_blobs.append(blob)
    print(f"got {len(clean_blobs)} non hidden blobs")

    # Build Index
    base = "<NOT A BASE>"
    html = """
    <html>
        <head>
            <title>Met Office Informatics Lab COVID-19 environmental data</title>
        </head>
        <body>
        <h1>Met Office Informatics Lab COVID-19 environmental data index</h1>
        <p>This is a very simple index of the files in this container/bucket.<p>
        <p>Stay up to date with new datasets, corrections, redactions and useful or important information by subscribing to our 
            <a href="https://groups.google.com/forum/#!forum/met-office-covid-19-data-and-platform-updates/join" >Google Groups mailing list</a></p>
        <p>For downloading numerous files we suggest using <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10">AzCopy</a> or other tools rather than this page.</p>
        <p>Please refer to the data <a href="LICENCE.txt">license</a> before use.</p>
    """

    def sorter(item):
        return (len(item.split('/')), item)

    for i, blob in enumerate(sorted(clean_blobs, key=sorter)):
        fbase = blob.rsplit('/', 1)[0] if blob.find('/') >= 0 else ''
        name = blob.rsplit('/', 1)[1] if blob.find('/') >= 0 else blob

        if not fbase == base:
            base = fbase

            jsid = "base-" + base.replace('/', '--')
            htmlstr = "" if i == 0 else "</ul>"
            htmlstr += f"\n\n<h3>{base}/<a style='font-size:50%' href='#{base}' onclick='$(\"#{jsid}\").toggle();false'>[show/hide]</a></h3>\n"
            htmlstr += f"<ul id='{jsid}'>" if jsid == "base-" else f"<ul id='{jsid}' style='display: none;'>"
            html += htmlstr

        htmlstr = f'\t<li><a title="{name}" href="{blob}">{name}</a></li>'
        html += htmlstr
    html += f"""</ul>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
    <p style="font-size:50%">Created at {datetime.datetime.now()}</p>
    </body></html>"""

    return html


def markdown_to_html(markdown_text):
    head = """
    <html>
    <head>
        <title>Met Office Informatics Lab COVID-19 environmental data</title>
    </head>
    <body>
    """
    body = markdown(markdown_text)
    foot = "</body></html>"
    html = (head+body+foot)

    return html


BlobEntry = namedtuple("Blob", ['path', 'content', 'mime'])


def upload_entries(entries, blob_access):

    print(f'Container: {blob_access.container}')
    if(DRY_RUN):
        print("*** DRY RUN ***")
        for blob_entry in entries:
            print(f"""

    ---------------------------------------------------
    {blob_entry.path} {blob_entry.mime}
    """)
    else:
        blob_service_client, container_client = blob_clients(blob_access)
        for blob_entry in entries:
            print(f'upload {blob_entry.path}...')
            blob_client = blob_service_client.get_blob_client(container=blob_access.container, blob=blob_entry.path)
            blob_client.upload_blob(
                blob_entry.content,
                overwrite=True,
                content_settings=ContentSettings(content_type=blob_entry.mime))
            print('uploaded')


def deploy_open_data():
    entries = []
    blob_access = account_details(os.environ['SIGNED_URL'])

    # Index
    index_html = build_index(blob_access)
    entries.append(
        BlobEntry('index.html', index_html, 'text/html')
    )

    # LICENCE
    with open('./open_LICENCE.txt', 'r') as fp:
        license_txt = fp.read()
    entries.append(BlobEntry('LICENCE.txt', license_txt, 'text/html'))

    # README
    with open('./README_data.md', 'r') as fp:
        readme_md = fp.read()
    readme_html = markdown_to_html(readme_md)
    entries += [
        BlobEntry('README_data.html', readme_html, 'text/html'),
        BlobEntry('README_data.md', readme_md,  'text/markdown'),
    ]

    # Technical docs
    with open('./README_data_air_quality.md', 'r') as fp:
        readme_aq_tech_md = fp.read()
    readme_aq_tech_html = markdown_to_html(readme_aq_tech_md)
    entries += [
        BlobEntry('README_data_air_quality.html', readme_aq_tech_html, 'text/html'),
        BlobEntry('README_data_air_quality.md', readme_aq_tech_md,  'text/markdown'),
    ]

    with open('README_data_processing.pdf', 'rb') as fp:
        tech_readme_bin = fp.read()
    entries.append(
        BlobEntry('README_data_processing.pdf', tech_readme_bin, 'application/pdf')
    )

    upload_entries(entries, blob_access)


def deploy_noncommercial_data():
    entries = []
    blob_access = account_details(os.environ['NON_COMMERCE_SIGNED_URL'])

    # Index
    index_html = build_index(blob_access)
    entries.append(
        BlobEntry('index.html', index_html, 'text/html')
    )

    # LICENCE
    with open('./noncommercial_LICENCE.txt', 'r') as fp:
        license_txt = fp.read()
    entries.append(BlobEntry('LICENCE.txt', license_txt, 'text/html'))

    # README
    with open('./README_non-commercial_data.md', 'r') as fp:
        readme_md = fp.read()
    readme_html = markdown_to_html(readme_md)
    entries += [
        BlobEntry('README.html', readme_html, 'text/html'),
        BlobEntry('README.md', readme_md,  'text/markdown'),
    ]

    upload_entries(entries, blob_access)


if __name__ == "__main__":
    deploy_open_data()
    deploy_noncommercial_data()
