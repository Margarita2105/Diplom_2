import requests
import curl
import allure


class ApiMethods:

    @staticmethod
    @allure.step('Создаем пользователя.')
    def user_new(email_new: str, password_new: str, name_new: str):
        return requests.post(curl.user_api, json={"email": email_new, "password": password_new, "name": name_new})

    @staticmethod
    @allure.step('Авторизуемся под созданным логином пользователя.')
    def login_user(email_user: str, password_user: str):
        return requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})

    @staticmethod
    @allure.step(
        'Меняем данные пользователя, запоминаем новые данные в переменную, меняем данные обратно для удаления пользователя после теста.')
    def data_user(email_user: str, password_user: str, email_new: str, password_new: str, name_new: str):
        response = requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})
        token = response.json()['accessToken']
        new_data = requests.patch(curl.data_user_api,
                                  json={"email": email_new, "password": password_new, "name": name_new},
                                  headers={'Authorization': token})
        response = requests.post(curl.login_user_api, json={"email": email_new, "password": password_new})
        token = response.json()['accessToken']
        requests.patch(curl.data_user_api,
                       json={"email": email_user, "password": password_user, "name": name_new},
                       headers={'Authorization': token})
        return new_data

    @staticmethod
    @allure.step('Удаляем созданного пользователя после прохождения теста.')
    def user_delete(email_delete, password_delete, name_delete):
        token_response = requests.post(curl.login_user_api,
                                       json={"email": email_delete, "password": password_delete, "name": name_delete})
        token = token_response.json()['accessToken']
        return requests.delete(curl.data_user_api, headers={'Authorization': token})

    @staticmethod
    @allure.step('Выходим из системы.')
    def logout_user(email_user: str, password_user: str):
        response = requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})
        token = response.json()['refreshToken']
        return requests.post(curl.user_logout, json={"token": token})

    @staticmethod
    @allure.step('Меняем данные незарегистрированного пользователя.')
    def data_user_logout(email_new: str, password_new: str, name_new: str):
        return requests.patch(curl.data_user_api, json={"email": email_new, "password": password_new, "name": name_new})
