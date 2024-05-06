import allure
import requests

from page.add_courier import AddCourier
from ursl import Urls


class TestAddCourier:

    @allure.title('Регестрация курьера')
    @allure.description('Позитивный сценарий регестрации курьера')
    def test_add_courier(self):


        payload = {"login": AddCourier.generate_random_string(5),
                   'password': "12345",
                   'firstName': 'Миша'
                   }
        response = requests.post(Urls.URL_HTTPS + Urls.URL_ADD_COURIER, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Регестрация курьера без логина')
    @allure.description('Проверка регестрации курьера без указаниля логина')
    def test_add_courier_without_login(self):
        payload = {"login": "",
                   "password": "12345",
                   "firstName": "Миша"
                   }
        response = requests.post(Urls.URL_HTTPS + Urls.URL_ADD_COURIER, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'


    @allure.title('Зоднаие двух одинаковых курьеров')
    @allure.description('Проверка регистрации друх одинаковых курьеров')
    def test_add_courier_repit_login(self):
        payload = {"login": AddCourier.generate_random_string(6),
                   'password': "12345",
                   'firstName': 'Мыша'
                   }
        response = requests.post(Urls.URL_HTTPS + Urls.URL_ADD_COURIER, data=payload)
        assert response.status_code == 201
        response = requests.post(Urls.URL_HTTPS + Urls.URL_ADD_COURIER, data=payload)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

