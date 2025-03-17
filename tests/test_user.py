from api.api_methods_user import ApiMethods
import allure
from api.data import Response, Data
import pytest
from api.helpers import data_email, data
from tests.conftest import register


class TestUserLogin:

    @allure.step('Создаем нового пользователя, проверяем ответ сервера.')
    def test_new_user(self, login):
        email_user = login[0]
        password_user = login[1]
        name_user = login[2]
        response = ApiMethods.user_new(email_user, password_user, name_user)
        success = response.json()['success']

        assert success == True and response.status_code == 200

    @allure.step('Проверяем невозможность создать двух одинаковых пользователей.')
    def test_user_two(self, login):
        email_user = login[0]
        password_user = login[1]
        name_user= login[2]
        ApiMethods.user_new(email_user, password_user, name_user)
        response = ApiMethods.user_new(email_user, password_user, name_user)

        assert response.json() == Response.code_403_new_user and response.status_code == 403

    @allure.step('Проверяем невозможность создать пользователя без логина, без пароля и без имени.')
    @pytest.mark.parametrize("email_user, password_user, name_user", [('', data, data), (data_email, '', data), (data_email, data, '')])
    def test_no_user_field_email_password(self, email_user, password_user, name_user):
        email_user = email_user
        password_user = password_user
        name_user = name_user
        response = ApiMethods.user_new(email_user, password_user, name_user)

        assert response.json() == Response.code_403_user_not_field and response.status_code == 403

    @allure.step('Авторизуемся под существующим логином пользователя, получаем success и ответ сервера.')
    def test_user_login(self, register):
        email = register[0]
        password = register[1]
        response = ApiMethods.login_user(email, password)
        success = response.json()['success']

        assert success == True and response.status_code == 200

    @allure.step('Проверяем невозможность авторизоваться передав некорректный email пользователя.')
    def test_incorrect_email_user_login(self, register):
        email_user = 'mail'
        password = register[1]
        response = ApiMethods.login_user(email_user, password)

        assert response.json() == Response.code_401_login_user and response.status_code == 401

    @allure.step('Проверяем невозможность авторизоваться передав некорректный пароль от email пользователя.')
    def test_incorrect_password_user_login(self, register):
        email_user = register[0]
        password = '123'
        response = ApiMethods.login_user(email_user, password)

        assert response.json() == Response.code_401_login_user and response.status_code == 401

    @allure.step('Проверяем изменение данных авторизованного пользователя.')
    @pytest.mark.parametrize("email, password, name, new_email, new_password, new_name",
                             [(Data.data_1), (Data.data_2), (Data.data_3), (Data.data_4)])
    def test_user_new_data(self, registration, email, password, name, new_email, new_password, new_name):
        response = ApiMethods.data_user(email, password, new_email, new_password, new_name)
        user_new = response.json()['user']

        assert user_new == {'email': new_email, 'name': new_name} and response.status_code == 200

    @allure.step('Проверяем изменение данных неавторизованного пользователя.')
    @pytest.mark.parametrize("email, password, name, new_email, new_password, new_name",
                             [(Data.data_1), (Data.data_2), (Data.data_3), (Data.data_4)])
    def test_user_new_data_logout(self, registration, email, password, name, new_email, new_password, new_name):
        response = ApiMethods.data_user_logout(new_email, new_password, new_name)

        assert response.json() == Response.code_401_data_logout_user and response.status_code == 401
