import allure
import requests

from data.login_courier import LoginCourier
from ursl import Urls


class TestLoginCourier:

    @allure.title('Авторизация курьера')
    @allure.description('Корректный ввод логина и пароля')
    def test_login_courier(self):
        login = LoginCourier.register_new_courier_and_return_login_password()
        payload = {'login': login[0],
                   'password': login[1]
                   }
        response = requests.post(Urls.URL_HTTPS + Urls.URL_LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and response.json()['id'] > 0



    @allure.title('Авторизация курьера')
    @allure.description('Ввод не существующего логина и корректного пароля')
    def test_error_in_correct_login_courier(self):
        login = LoginCourier.register_new_courier_and_return_login_password()
        payload = {'login': login[1],
                   'password': login[1]
                   }
        response = requests.post(Urls.URL_HTTPS + Urls.URL_LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'



    @allure.title('Авторизация курьера')
    @allure.description('Ввод логина без пароля')
    def test_error_empty_password_courier(self):
        login = LoginCourier.register_new_courier_and_return_login_password()
        payload = {'login': login[0],
                   'password': ''}
        response = requests.post(Urls.URL_HTTPS + Urls.URL_LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

