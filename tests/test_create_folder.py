import pytest
from utils.box_client import create_folder

def test_create_folder():
    response = create_folder("Test_Automation_Folder")
    assert response.get("id") is not None, "Folder creation failed"
    print(f"Created Folder ID: {response['id']}")
