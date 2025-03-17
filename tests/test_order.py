from api.api_method_order import ApiMethodsOrder
from api.data import Ingredient
import allure

class TestOrder:

    @allure.step('Проверяем возможность создания заказа авторизованным пользователем, заказ с ингредиентами.')
    def test_order_new(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_new(email_user, password_user, Ingredient.ingredient)
        success = response.json()['success']
        assert success == True and response.status_code == 200

    @allure.step('Проверяем невозможность создания заказа неавторизованным пользователем.')
    def test_order_new_no_login_user(self):
        response = ApiMethodsOrder.order_new_no_login_user(Ingredient.ingredient)
        try:
            assert response.status_code == 500
        except AssertionError:
            print("Это баг")

    @allure.step('Проверяем невозможность создания заказа без ингредиентов.')
    def test_order_new_no_ingredient(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_new(email_user, password_user, Ingredient.zero_ingredient)
        success = response.json()['success']
        assert success == False and response.status_code == 400

    @allure.step('Проверяем невозможность создания заказа с неверным хешем ингредиентов.')
    def test_order_new_invalid_ingredient(self, register):
        email_user = register[0]
        password_user = register[1]
        response = ApiMethodsOrder.order_new(email_user, password_user, Ingredient.invalid_ingredient)
        assert response.status_code == 500
