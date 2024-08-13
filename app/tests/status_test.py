from tests import client


def test_status():
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json() == {
        'status': 'ok',
    }
