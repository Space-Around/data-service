import requests


class StorageWrap:
    def __init__(self, ip_addr = None):
        if ip_addr:
            self._ip_addr = ip_addr
        else:
            raise ValueError('Set ip address')

    def store(self, payload):
        url = f'{self._ip_addr}/store'
        data = {'payload': payload}

        response = requests.post(url, json=data)
        json_response = response.json()

        status = json_response['status']

        if status.find('success') != -1:
            return True
        else:
            return False


    def clear(self):
        url = f'{self._ip_addr}/clear'

        response = requests.post(url)
        json_response = response.json()

        status = json_response['status']

        if status.find('success') != -1:
            return True
        else:
            return False

    def read(self):
        url = f'{self._ip_addr}/read'

        response = requests.post(url)
        json_response = response.json()

        status = json_response['status']

        if status.find('success') != -1:
            payload = json_response['payload']
            return payload
        else:
            return None