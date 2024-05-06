import allure
import pytest
import requests

from page.add_order import AddOrder
from ursl import Urls


class TestAddOrder:

    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа с разными цветами самоката через параметризацию')
    @pytest.mark.parametrize('result', AddOrder.result)
    def test_add_order(self, result):
        response = requests.post(Urls.URL_HTTPS + Urls.URL_ADD_ORDER, json=result)
        assert response.status_code == 201 and response.json()['track'] is not None
