import whisper
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

model = whisper.load_model("turbo")
result = model.transcribe('/Users/mroshan3/Downloads/New Recording.m4a')
print(result["text"])
# write result of text to a file
with open('output.txt', 'w') as f:
    f.write(result["text"])

# Connection string to your Azure Storage account
connection_string = ""

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "mroshan3-container"

# upload local file to azure blob storage
blob_name = "output.txt"
# Read the data to upload
with open('output.txt', 'rb') as data:
    data = data.read()
    
# Create a BlobClient
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload the data
blob_client.upload_blob(data)

print(f"Data uploaded to {blob_name} in container {container_name}")
