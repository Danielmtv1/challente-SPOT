from azure.core.exceptions import ResourceNotFoundError
from core.config.azure_conection import blob_service_client


def test_container():
    container_names = []

    try:
        containers = blob_service_client.list_containers()
        if containers:
            print("Connection to Azure Blob Storage established successfully.")
            for container in containers:
                print(container.name)
                container_names.append(container.name)
        else:
            print("No containers found in the storage account.")

    except ResourceNotFoundError:
        print("Failed to establish connection to Azure Blob Storage."
              " Please check the connection string and access permissions.")
    return container_names
