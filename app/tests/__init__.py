from fastapi.testclient import TestClient
from initialize import create_app

client = TestClient(create_app())
