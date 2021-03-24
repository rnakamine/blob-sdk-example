import os

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_STORAGE_BLOB_CONTAINER_NAME')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)


def main():
    # List the blobs in container
    print("\nListing blobs...")
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)


if __name__ == '__main__':
    main()
