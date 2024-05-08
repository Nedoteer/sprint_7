import allure
import requests

from ursl import Urls


class TestOrderList:

    @allure.title('Список заказов')
    @allure.description('Проверяем что в тело ответа возвращается список заказов')
    def test_order_list(self):
        response = requests.get(Urls.URL_HTTPS + Urls.URL_ORDER_LIST)
        assert response.status_code == 200 and response.json()['orders'] is not None