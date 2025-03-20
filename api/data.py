class Response:
    code_401_login_user = {"success": False, "message": "email or password are incorrect"}
    code_401_data_logout_user = {'success': False, 'message': 'You should be authorised'}
    code_403_new_user = {'success': False, 'message': 'User already exists'}
    code_403_user_not_field = {"success": False, "message": "Email, password and name are required fields"}
    code_401_list_order_logout_user = {"success": False, "message": "You should be authorised"}

class Data:
    data_1 = ['data_mail_u@mail.com', 'data', 'name_data', 'new_data@mail.com', 'newdata', 'newndata']
    data_2 = ['data_mail_u@mail.com', 'data', 'name_data', 'new_data@mail.com', 'data', 'name_data']
    data_3 = ['data_mail_u@mail.com', 'data', 'name_data', 'data_mail_u@mail.com', 'newdata', 'name_data']
    data_4 = ['data_mail_u@mail.com', 'data', 'name_data', 'data_mail_u@mail.com', 'data', 'newndata']

class Ingredient:
    ingredient = ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
    invalid_ingredient = ["61c0c5a71d1f82001"]
    zero_ingredient = []
