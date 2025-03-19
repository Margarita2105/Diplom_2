import requests
import curl
import allure

class ApiMethodsOrder:

    @staticmethod
    @allure.step('Авторизуемся, получаем токен.')
    def user_login(email_user, password_user):
        response = requests.post(curl.login_user_api, json={"email": email_user, "password": password_user})
        return  response.json()['accessToken']

    @staticmethod
    @allure.step('Создаем новый заказ авторизованным пользователем.')
    def order_new(token, ingredients):
        return requests.post(curl.orders_api, json={"ingredients": ingredients}, headers={'Authorization': token})

    @staticmethod
    @allure.step('Создаем новый заказ неавторизованным пользователем.')
    def order_new_no_login_user(ingredients):
        return requests.post(curl.orders_api, json={"ingredients": ingredients})
