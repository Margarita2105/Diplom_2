import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Получаем список заказов авторизованным пользователем.')
    def order_list(email_user, password_user):
        response = requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})
        token = response.json()['accessToken']
        return requests.get(curl.orders_api, headers={'Authorization': token})

    @staticmethod
    @allure.step('Получаем список заказов неавторизованным пользователем.')
    def order_list_no_login_user():
        return requests.get(curl.orders_api)
