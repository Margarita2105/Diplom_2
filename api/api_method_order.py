import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Создаем новый заказ авторизованным пользователем.')
    def order_new(email_user, password_user, ingredients):
        response = requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})
        token = response.json()['accessToken']
        return requests.post(curl.orders_api, json={"ingredients": ingredients}, headers={'Authorization': token})

    @staticmethod
    @allure.step('Создаем новый заказ неавторизованным пользователем.')
    def order_new_no_login_user(ingredients):
        return requests.post(curl.orders_api, json={"ingredients": ingredients})
