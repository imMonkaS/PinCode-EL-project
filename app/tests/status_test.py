from fastapi.testclient import TestClient

from initialize import create_app

client = TestClient(create_app())


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {
        'status': 'ok',
    }
