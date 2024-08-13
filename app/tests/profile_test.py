from datetime import date

from internal.db.db import Database
from tests import client


Database.fill_database_with_test_data()
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
      "login": "login",
      "password": "password",
      "last_name": "last_name",
      "first_name": "first_name",
      "middle_name": "middle_name",
      "birth_date": "1998-08-20",
      "work_experience": 5
}
get_create_test_data = create_test_data.copy()
get_create_test_data['age'] = 25
get_create_test_data.pop('password')


# create
def test_get():
    response = client.get('/user/profile/0')
    assert response.status_code == 200
    assert response.json() == get_test_data


def test_create():
    post_response = client.post('/user/profile/', json=create_test_data)
    print(post_response.json())
    get_response = client.get(f'/user/profile/{post_response.json()['user_id']}')
    assert get_response.status_code == 200
    assert get_response.json() == get_create_test_data

