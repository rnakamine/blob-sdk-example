import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def main():
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    containers = blob_service_client.list_containers()
    for container in containers:
        print(
            f"Name: {container['name']} Last Modified: {container['last_modified']}")


if __name__ == '__main__':
    main()
