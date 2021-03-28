import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def main():
    container_name = 'testnakamine'
    blob_name = 'sample.txt'

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(
        container_name, blob=blob_name)

    if blob_client.exists():
        print('Exists')
    else:
        print('Not exists')


if __name__ == '__main__':
    main()
