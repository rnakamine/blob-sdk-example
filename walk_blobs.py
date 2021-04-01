import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def main():
    container_name = 'testnakamine'
    blob_name = 'sample.txt'

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(
        'company-settings')

    list_blobs = container_client.walk_blobs(
        name_starts_with=None, delimiter='/')
    for b in list_blobs:
        print(b.name)


if __name__ == '__main__':
    main()
