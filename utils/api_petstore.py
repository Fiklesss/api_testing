import requests
from io import BytesIO
from utils.http_methods import Http_methods
from utils.logger import Logger

base_url = 'https://petstore.swagger.io/v2'
class User_petStore_api():

    """POST: Создание пользователя"""
    @staticmethod
    def create_new_user():

        json_new_user = {
  "id": 0,
  "username": "test_user",
  "firstName": "Fiklesss",
  "lastName": "Monomishka",
  "email": "",
  "password": "333",
  "phone": "",
  "userStatus": 0
}
        # конструктор URL
        post_resource = '/user'
        post_url = base_url + post_resource
        print(post_url)
        # log_point
        Logger.add_request(url=post_url, method='POST', comment='Создание пользователя')
        # результат
        post_result = Http_methods.post(post_url, json_new_user)
        print(post_result.text)

        return post_result

    """GET-POST: Провека создание пользователя"""
    @staticmethod
    def check_nickname_user(nickname):
        # конструктор URL
        get_resource = f'/user/{nickname}'
        get_url = base_url + get_resource
        print(get_url)
        # log_point
        Logger.add_request(url=get_url, method='GET', comment='Проверка')
        # результат
        get_result = Http_methods.get(get_url)
        print(get_result.text)

        return get_result

    """PUT: Изменение данных пользователя"""
    @staticmethod
    def update_data_user(nickname):
        json_update_data_user = {
            "id": 0,
            "username": "Tester_user",
            "firstName": "Fiklesss",
            "lastName": "Monomishka",
            "email": "f1kles@mail.ru",
            "password": "333",
            "phone": "+7(777)77-77",
            "userStatus": 0
        }
        # конструктор URL
        put_resource = f'/user/{nickname}'
        put_url = base_url + put_resource
        print(put_url)
        # log_point
        Logger.add_request(url=put_url, method='PUT', comment='Изменение данных пользователя')
        # результат
        put_result = Http_methods.put(put_url, json_update_data_user)
        print(put_result.text)

        return put_result

    """Get: Login"""
    @staticmethod
    def login_user(nickname, pas):

        # конструктор URL
        login_resource = '/user/login'
        login_url = f'{base_url}{login_resource}?username={nickname}&password={pas}'
        print(login_url)
        # log_point
        Logger.add_request(url=login_url, method='GET', comment='Вход в учетную запись')
        # результат
        login_result = Http_methods.get(login_url)
        print(login_result.text)

        return login_result

    """Get: Logout"""
    @staticmethod
    def logout_user():

        # конструктор URL
        logout_resource = '/user/logout'
        logout_url = base_url + logout_resource
        print(logout_url)
        # log_point
        Logger.add_request(url=logout_url, method='GET', comment='Выход из учетной записи')
        # результат
        logout_result = Http_methods.get(logout_url)
        print(logout_result.text)

        return logout_result

    """DELETE: Удаление"""
    @staticmethod
    def delete_user(nickname):

        # конструктор URL
        delete_resource = f'/user/{nickname}'
        delete_url = base_url + delete_resource
        print(delete_url)
        # log_point
        Logger.add_request(url=delete_url, method='DELETE', comment='Удаление пользователя')
        # результат
        delete_result = Http_methods.delete(delete_url)
        print(delete_result.text)

        return delete_result

class Pet_petStore_api():

    """POST: Создание питомца"""
    @staticmethod
    def create_pet():
        json_body_create_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "pending"
}
        post_resourse = '/pet'
        post_url = base_url + post_resourse
        # log_point
        Logger.add_request(url=post_url, method='POST', comment='Создание питомца')
        post_result = Http_methods.post(post_url, json_body_create_pet)

        print(post_url)
        return post_result

    """POST: Загрузка изображения питомца"""
    @staticmethod
    def upload_image_pet(id_pet, image_url):


        response = requests.get(image_url)
        if response.status_code == 200:
            image_url = BytesIO(response.content)
        files = {
            "file": ("animal-dog.png", image_url, "image/png")
        }
        data = {
            "additionalMetadata": "Фото для питомца"
        }

        post_upload_resourse = f'/pet/{id_pet}/uploadImage'
        post_upload_url = base_url + post_upload_resourse
        # log_point
        Logger.add_request(url=post_upload_url, method='POST', comment='Загрузка изображения')
        post_upload_result = Http_methods.post(post_upload_url,files=files, data=data)

        print(post_upload_url)
        return post_upload_result

    """POST: для обновления данных в магазине (через form-data)"""
    @staticmethod
    def update_data_pet(id_pet, name, status):
        data_form = {
            "name": name,
            "status": status
        }
        post_form_data_resourse = f'/pet/{id_pet}'
        post_form_data_url = base_url + post_form_data_resourse
        # log_point
        Logger.add_request(url=post_form_data_url, method='POST', comment='Обновление данных через form-data')
        post_form_data_result = Http_methods.post(post_form_data_url, data=data_form)

        print(post_form_data_url)
        return post_form_data_result

    """PUT: Изменение данных питомца (через json)"""
    @staticmethod
    def update_pet(id_pet, photo_url):
        json_body_update_pet = {
            "id": id_pet,
            "category": {
                "id": 0,
                "name": "animals"
            },
            "name": "dog",
            "photoUrls": [photo_url],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        put_resourse = '/pet'
        put_url = base_url + put_resourse
        # log_point
        Logger.add_request(url=put_url, method='POST', comment='Обновление данных через json')
        put_result = Http_methods.put(put_url, json_body_update_pet)

        print(put_url)
        return put_result

    """DELETE: Удаление питомца"""
    @staticmethod
    def delete_pet(id_pet):
        delete_resourse = f'/pet/{id_pet}'
        delete_url = base_url + delete_resourse
        # log_point
        Logger.add_request(url=delete_url, method='POST', comment='Удаление питомца')
        delete_result = Http_methods.delete(delete_url)

        print(delete_url)
        return delete_result

# #################################################

    """GET: Проверка info питомца"""
    @staticmethod
    def check_info_pet(id_pet):
        get_resourse = f'/pet/{id_pet}'
        get_url = base_url + get_resourse
        # log_point
        Logger.add_request(url=get_url, method='POST', comment='Проверка')
        get_result = Http_methods.get(get_url)

        print(get_url)
        return get_result

    """GET: Проверка наличие питомцев по статусу"""
    @staticmethod
    def check_status_pets(status):
        get_status_resourse = f'/pet/findByStatus?status={status}'
        get_status_url = base_url + get_status_resourse
        # log_point
        Logger.add_request(url=get_status_url, method='POST', comment='проверка по статусу')
        get_status_result = Http_methods.get(get_status_url)

        print(get_status_url)
        return get_status_result