import requests
from utils.logger import Logger

class Http_methods():

    headers = {'Content-Type': 'application/json'}
    cookies = ""

    """GET"""
    @staticmethod
    def get(url):
        #Logger.add_request(url, method='GET')
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result

    """POST"""
    @staticmethod
    def post(url, body=None, files=None, data=None):
        #Logger.add_request(url, method='POST')


        if data or files:
            headers = Http_methods.headers.copy()
            if data:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            result = requests.post(url, data=data, files=files, headers=headers, cookies=Http_methods.cookies)
        else:
            headers = Http_methods.headers.copy()
            headers['Content-Type'] = 'application/json'  # Устанавливаем Content-Type для JSON явно
            result = requests.post(url, json=body, headers=headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result
    """PUT"""
    @staticmethod
    def put(url, body):
        #Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result
    """DELETE"""
    @staticmethod
    def delete(url):
        #Logger.add_request(url, method='DELETE')
        result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(result)
        return result