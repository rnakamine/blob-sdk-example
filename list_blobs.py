import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def main():
    container_name = 'testnakamine'
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    blobs = container_client.list_blobs()
    for blob in blobs:
        print(blob['name'], blob['last_modified'])


if __name__ == '__main__':
    main()
