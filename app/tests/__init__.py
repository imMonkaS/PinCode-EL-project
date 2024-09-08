from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from initialize import create_app

client = TestClient(create_app())
async_client = AsyncClient(transport=ASGITransport(app=create_app()), base_url='http://127.0.0.1:7070/api/')
