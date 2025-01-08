from utils.api_petstore import User_petStore_api, Pet_petStore_api
import pytest
from requests import Response
from utils.checking import Checking
from utils.logger import Logger



class Test_create_user():
    """Body"""
    def setup_method(self):
        self.user_data = {} # Словарь для хранения данных пользователя
    def extract_body_user(self, response):
        json_data = response.request.body  # вызываем тело запроса
        self.user_data = eval(json_data)  # Сохраняет тело в объект

    """Тесты"""
    def test_create_new_user(self):
        print('Метод POST')
        result_post: Response = User_petStore_api.create_new_user()
        self.extract_body_user(result_post)
        #проверка
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)

        print('Метод GET-POST')
        result_get: Response = User_petStore_api.check_nickname_user(self.user_data['username'])
        # проверка
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)

        print('Метод PUT')
        result_put: Response = User_petStore_api.update_data_user(self.user_data['username'])
        self.extract_body_user(result_put)
        # проверка
        Checking.check_status_code(result_put, 200)
        print(result_put.status_code)

        print('Метод GET-PUT')
        result_get: Response = User_petStore_api.check_nickname_user(self.user_data['username'])
        # проверка
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)

        print('Метод GET-login')
        result_login: Response = User_petStore_api.login_user(self.user_data['username'], self.user_data['password'])
        # проверка
        Checking.check_status_code(result_login, 200)
        print(result_login.status_code)

        print('Метод GET-logout')
        result_logout: Response = User_petStore_api.logout_user()
        # проверка
        Checking.check_status_code(result_logout, 200)
        print(result_logout.status_code)

        print('Метод DELETE')
        result_delete: Response = User_petStore_api.delete_user(self.user_data['username'])
        # проверка
        Checking.check_status_code(result_delete, 200)
        print(result_delete.status_code)

        print('Метод GET-DELETE')
        result_get: Response = User_petStore_api.check_nickname_user(self.user_data['username'])
        # проверка
        Checking.check_status_code(result_get, 404)
        print(result_get.status_code)

class Test_create_pet():

    def test_create_pet(self):
        photo_url = "https://dasart.ru/userdata/image/fb/d4/fbd468ec4ad4c0f28ef9a4f2a352b84e.webp"

        """POST"""
        print('POST: создание PET')
        result_post: Response = Pet_petStore_api.create_pet()
        id_pet = result_post.json().get("id")
        status_pet = result_post.json().get("status")
        print(result_post.text)
        #Проверки
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)

        """GET-POST"""
        print('GET-POST: info питомца')
        result_get: Response = Pet_petStore_api.check_info_pet(id_pet)
        print(result_get.text)
        # Проверки
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)

        """GET-POST"""
        print('GET_POST: проверка по статусу питомца в списке магазина')
        result_get_status: Response = Pet_petStore_api.check_status_pets(status_pet)
        pets_list = result_get_status.json()
        if any(pet.get('id') == id_pet for pet in pets_list):
            print('Питомец есть в списке!')
        else:
            print('Питомец отсутствует!')
        # Проверки
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)


        """POST"""
        print('POST: обновления данных питомца в магазине')
        result_post_update: Response = Pet_petStore_api.update_data_pet(id_pet, 'dog', 'available')
        print(result_post_update.text)
        # Проверки
        Checking.check_status_code(result_post_update, 200)
        print(result_post_update.status_code)

        """GET-POST"""
        print('GET-POST: проверка записи данных')
        result_get: Response = Pet_petStore_api.check_info_pet(id_pet)
        print(result_get.text)
        # Проверки
        Checking.check_json_value(result_get, ['name'], 'dog')
        Checking.check_json_value(result_get, ['status'], 'available')
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)

        """POST"""
        print('POST: загрузка изображения')
        result_upload_post: Response = Pet_petStore_api.upload_image_pet(id_pet, photo_url)
        print(result_upload_post.text)
        #Проверки
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)

        """PUT"""
        print('PUT: изменение данных')
        result_put: Response = Pet_petStore_api.update_pet(id_pet, photo_url)
        print(result_put.text)
        # Проверки
        Checking.check_status_code(result_put, 200)
        print(result_put.status_code)

        """GET-PUT"""
        print('GET-POST: проверка записи данных')
        result_get: Response = Pet_petStore_api.check_info_pet(id_pet)
        print(result_get.text)
        # Проверки
        Checking.check_json_value(result_get, ['category', 'name'], 'animals')
        Checking.check_json_value(result_get, ['photoUrls'], [photo_url])
        Checking.check_status_code(result_get, 200)
        print(result_get.status_code)

        """DELETE"""
        print('DELETE: Удаление питомца')
        result_delete: Response = Pet_petStore_api.delete_pet(id_pet)
        print(result_delete.text)
        #Проверки
        Checking.check_status_code(result_delete, 200)
        print(result_get.status_code)

        """GET-DELETE"""
        print('GET-DELETE: проверка на отсутствие пользователя')
        result_get: Response = Pet_petStore_api.check_info_pet(id_pet)
        print(result_get.text)
        # Проверки
        Checking.check_status_code(result_get, 404)
        print(result_get.status_code)








