import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def main():
    container_name = 'testnakamine3'
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_service_client.create_container(container_name)


if __name__ == '__main__':
    main()
