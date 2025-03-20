import pytest
from api.helpers import generate_random_string
from api.helpers import register_new_user_and_return_login_password
from api.api_methods_user import ApiMethods
from api.data import Data
import requests
import curl

@pytest.fixture
def login():
    email = generate_random_string(10)+'@mail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)
    login_pass = [email, password, name]

    yield login_pass
    ApiMethods.user_delete(email, password, name)

@pytest.fixture
def register():
    register = register_new_user_and_return_login_password()

    yield register
    ApiMethods.user_delete(register[0], register[1], register[2])

@pytest.fixture
def registration():
    payload = {
        "email": Data.data_1[0],
        "password": Data.data_1[1],
        "name": Data.data_1[2]
    }
    requests.post(curl.user_api, data=payload)
    registration = [Data.data_1[0], Data.data_1[1], Data.data_1[2]]

    yield registration
    ApiMethods.user_delete(registration[0], registration[1], registration[2])
