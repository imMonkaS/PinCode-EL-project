from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from tests import client

create_test_data = {
    'login': 'login',
    'password': 'password',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'middle_name': 'middle_name',
    'birth_date': '1998-08-20',
    'work_experience': 5
}

get_create_test_data = {
    'status': 200,
    'message': 'Success',
    'data': {
        'login': 'login',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'birth_date': '1998-08-20',
        'work_experience': 5,
        'age': relativedelta(datetime.today(), date(1998, 8, 20)).years
    }
}

create_test_data_least_params = {
    'login': 'login',
    'password': 'password',
    'first_name': 'first_name',
    'birth_date': '1998-08-20',
}

get_create_test_data_least_params = {
    'status': 200,
    'message': 'Success',
    'data': {
        'login': 'login',
        'last_name': None,
        'first_name': 'first_name',
        'middle_name': None,
        'birth_date': '1998-08-20',
        'work_experience': 0,
        'age': relativedelta(datetime.today(), date(1998, 8, 20)).years
    }
}

validation_error_response = {
    'message': 'Pydantic validation error',
    'error_code': [
        {
            'type': 'missing',
            'loc': [
                'body',
                'password'
            ],
            'msg': 'Field required',
            'input': {
                'login': 'string',
                'first_name': 'string',
                'birth_date': '2024-08-14'
            }
        }
    ]
}


def test_create_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    get_response = client.get(f"/user/profile/{post_response.json()['data']['user_id']}")
    assert get_response.status_code == 200
    assert get_response.json() == get_create_test_data


def test_create_user_with_least_params():
    post_response = client.post('/user/profile/', json=create_test_data_least_params)
    get_response = client.get(f"/user/profile/{post_response.json()['data']['user_id']}")
    assert get_response.status_code == 200
    assert get_response.json() == get_create_test_data_least_params


def test_update_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    patch_response = client.patch(f"/user/profile/{post_response.json()['data']['user_id']}", json={
        'login': 'login2',
        'password': 'password2',
        'work_experience': 12
    })
    assert patch_response.json() == {
        'status': 200,
        'message': 'Success',
        'data': {
            'user_id': post_response.json()['data']['user_id'],
            'action': 'Updated',
            'updates_amount': 3
        }
    }
    get_response = client.get(f"/user/profile/{post_response.json()['data']['user_id']}")
    assert get_response.json() == {
        'status': 200,
        'message': 'Success',
        'data': {
            'login': 'login2',
            'last_name': 'last_name',
            'first_name': 'first_name',
            'middle_name': 'middle_name',
            'birth_date': '1998-08-20',
            'work_experience': 12,
            'age': relativedelta(datetime.today(), date(1998, 8, 20)).years
        }
    }


def test_replace_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    client.put(f"/user/profile/{post_response.json()['data']['user_id']}", json={
        'login': 'replace',
        'password': 'replace',
        'first_name': 'replace',
        'birth_date': '1998-08-20'
    })
    get_response = client.get(f"/user/profile/{post_response.json()['data']['user_id']}")
    assert get_response.json() == {
        'status': 200,
        'message': 'Success',
        'data': {
            'login': 'replace',
            'last_name': None,
            'first_name': 'replace',
            'middle_name': None,
            'birth_date': '1998-08-20',
            'work_experience': 0,
            'age': relativedelta(datetime.today(), date(1998, 8, 20)).years
        }
    }


def test_delete_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    client.delete(f"/user/profile/{post_response.json()['data']['user_id']}")
    get_response = client.get(f"/user/profile/{post_response.json()['data']['user_id']}")
    assert get_response.status_code == 404
    assert get_response.json() == {
        'error_code': 3,
        'message': 'User does not exist'
    }


def test_get_not_exist_user():
    get_response = client.get('/user/profile/9999999')
    assert get_response.status_code == 404
    assert get_response.json() == {
        'error_code': 3,
        'message': 'User does not exist'
    }


def test_validation_error():
    post_response = client.post('/user/profile/', json={
        'login': 'string',
        'first_name': 'string',
        'birth_date': '2024-08-14'
    })
    assert post_response.status_code == 422
    assert post_response.json() == validation_error_response
