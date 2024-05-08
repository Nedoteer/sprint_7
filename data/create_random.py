
import random
import string

import allure


class CreateRandom:

    @allure.step("Создание случайных комбинаций логина,пароля")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string