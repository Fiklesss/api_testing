from requests import Response
from utils.logger import Logger

class Checking():
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert response.status_code == status_code, f"Ожидался статус код {status_code}, но получили {response.status_code}"
        if response.status_code == status_code:
            print(f'Статус код: {status_code}')
        else:
            print('Провал! Статус код неверен!')

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        json_data = response.json()
        for key in field_name:
            json_data = json_data.get(key)
            if json_data is None:
                print(f"Ключ '{key}' не найден в  JSON-ответе.")

        assert json_data == expected_value
        print(f"Значение '{field_name[-1]}' соответствует ожидаемому: '{expected_value}'")

