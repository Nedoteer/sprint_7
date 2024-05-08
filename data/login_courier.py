import allure
import requests
import random
import string

from ursl import Urls


class LoginCourier:


    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @allure.step('Метод регистрации нового курьера, возвращает список из логина и пароля')
    def register_new_courier_and_return_login_password():

        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        @allure.step('Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки')
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls. URL_HTTPS + Urls.URL_ADD_COURIER, data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass