from internal.repositories.db.db import UserDatabase
from tests import client

UserDatabase.fill_database_with_test_data()
get_test_data = {
    'login': 'MonkaS',
    'last_name': 'naumov',
    'first_name': 'danya',
    'middle_name': 'alexeevich',
    'birth_date': '2005-01-25',
    'work_experience': 1,
    'age': 19
}

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
    'login': 'login',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'middle_name': 'middle_name',
    'birth_date': '1998-08-20',
    'work_experience': 5,
    'age': 25
}

create_test_data_least_params = {
    'login': 'login',
    'password': 'password',
    'first_name': 'first_name',
    'birth_date': '1998-08-20',
}
get_create_test_data_least_params = {
    'login': 'login',
    'last_name': None,
    'first_name': 'first_name',
    'middle_name': None,
    'birth_date': '1998-08-20',
    'work_experience': 0,
    'age': 25
}


# create
def test_get_user():
    response = client.get('/user/profile/0')
    assert response.status_code == 200
    assert response.json() == get_test_data


def test_create_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    get_response = client.get(f"/user/profile/{post_response.json()['user_id']}")
    assert get_response.status_code == 200
    assert get_response.json() == get_create_test_data


def test_create_user_with_least_params():
    post_response = client.post('/user/profile/', json=create_test_data_least_params)
    get_response = client.get(f"/user/profile/{post_response.json()['user_id']}")
    assert get_response.status_code == 200
    assert get_response.json() == get_create_test_data_least_params


def test_update_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    patch_response = client.patch(f"/user/profile/{post_response.json()['user_id']}", json={
        'login': 'login2',
        'password': 'password2',
        'work_experience': 12
    })
    assert patch_response.json() == {
        'user_id': post_response.json()['user_id'],
        'action': 'Updated',
        'Updates_amount': 3
    }
    get_response = client.get(f"/user/profile/{post_response.json()['user_id']}")
    assert get_response.json() == {
        'login': 'login2',
        'last_name': 'last_name',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'birth_date': '1998-08-20',
        'work_experience': 12,
        'age': 25
    }


def test_replace_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    client.put(f"/user/profile/{post_response.json()['user_id']}", json={
        'login': 'replace',
        'password': 'replace',
        'first_name': 'replace',
        'birth_date': '1998-08-20'
    })
    get_response = client.get(f"/user/profile/{post_response.json()['user_id']}")
    assert get_response.json() == {
        'login': 'replace',
        'last_name': None,
        'first_name': 'replace',
        'middle_name': None,
        'birth_date': '1998-08-20',
        'work_experience': 0,
        'age': 25
    }


def test_delete_user():
    post_response = client.post('/user/profile/', json=create_test_data)
    client.delete(f"/user/profile/{post_response.json()['user_id']}")
    get_response = client.get(f"/user/profile/{post_response.json()['user_id']}")
    assert get_response.status_code == 404
    assert get_response.json() == {
        'detail': 'User does not exist'
    }
