import requests
import os
from utils.box_client import create_folder
from dotenv import load_dotenv

load_dotenv()

BOX_ACCESS_TOKEN = os.getenv("BOX_ACCESS_TOKEN")
BASE_URL = "https://upload.box.com/api/2.0/files/content"
HEADERS = {"Authorization": f"Bearer {BOX_ACCESS_TOKEN}"}

def test_upload_file():
    folder_response = create_folder("Test_Upload_Folder")
    folder_id = folder_response.get("id")
    
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("This is a test file for Box API.")

    files = {
        "attributes": (None, f'{{"name":"test_file.txt","parent":{{"id":"{folder_id}"}}}}'),
        "file": open(file_path, "rb")
    }

    response = requests.post(BASE_URL, files=files, headers=HEADERS)
    assert response.status_code == 201, "File upload failed"
    print(f"Uploaded File ID: {response.json()['entries'][0]['id']}")
