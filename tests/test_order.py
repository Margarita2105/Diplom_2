from api.api_method_order import ApiMethodsOrder
from api.data import Ingredient
import allure
import pytest

class TestOrder:

    @allure.title('Проверяем возможность создания заказа авторизованным пользователем, заказ с ингредиентами.')
    def test_order_new(self, register):
        email_user = register[0]
        password_user = register[1]
        token = ApiMethodsOrder.user_login(email_user, password_user)
        response = ApiMethodsOrder.order_new(token, Ingredient.ingredient)
        success = response.json()['success']
        assert success == True and response.status_code == 200

    @allure.title('Проверяем невозможность создания заказа неавторизованным пользователем.')
    def test_order_new_no_login_user(self):
        with pytest.raises(AssertionError):
            response = ApiMethodsOrder.order_new_no_login_user(Ingredient.ingredient)
            assert response.status_code == 500

    @allure.title('Проверяем невозможность создания заказа без ингредиентов.')
    def test_order_new_no_ingredient(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_new(email_user, password_user, Ingredient.zero_ingredient)
        success = response.json()['success']
        assert success == False and response.status_code == 400

    @allure.title('Проверяем невозможность создания заказа с неверным хешем ингредиентов.')
    def test_order_new_invalid_ingredient(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_new(email_user, password_user, Ingredient.invalid_ingredient)
        assert response.status_code == 500
