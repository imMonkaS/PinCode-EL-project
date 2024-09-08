from datetime import date, datetime

import pytest
from dateutil.relativedelta import relativedelta
from tests import async_client

user_profile_path = '/v1/user/profile/'


create_test_data = {
    'login': 'login',
    'password': 'password',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'middle_name': 'middle_name',
    'birth_date': '2005-01-25',
    'work_experience': 5
}

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_user_crud():
    get_response = await async_client.get(f'{user_profile_path}1')
    assert get_response.status_code == 200
    age = relativedelta(datetime.today(), date(2005, 1, 25)).years
    assert get_response.json()['data']['age'] == age
