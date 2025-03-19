from api.api_method_order_user import ApiMethodsOrder
import allure
from api.data import Response


class TestOrderUserList:

    @allure.title('Проверяем получение списка заказов авторизованным пользователем.')
    def test_order_list(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_list(email_user, password_user)
        success = response.json()['success']
        assert success == True and response.status_code == 200

    @allure.title('Проверяем невозможность получение списка заказов неавторизованным пользователем.')
    def test_order_list_no_login_user(self):
        response = ApiMethodsOrder.order_list_no_login_user()
        assert response.json() == Response.code_401_list_order_logout_user and response.status_code == 401
