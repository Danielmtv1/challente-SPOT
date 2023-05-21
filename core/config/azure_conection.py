from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName=stdevtestaccount;"
    "AccountKey=M7G3GR77/JsCrWZJq6p5Nku0YiiS5o9WiwMTSjchDhfz9u2+mHS+"
    "rv51gdhVHHMDzx3kWlHQjNAB+AStpT49LQ=="
)
blob_service_client = BlobServiceClient.from_connection_string(
    CONNECTION_STRING
)
container_name = "test-container"
