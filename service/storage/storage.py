import os
import sys


class Storage:
    storage_name = 'storage'
    storage_ext = 'txt'

    @staticmethod
    def store(payload=None):
        print(f'store: {payload}')
        with open(f'{Storage.storage_name}.{Storage.storage_ext}', 'w') as file:
            file.write(payload)

    @staticmethod
    def read():
        print('read')
        payload = ''

        with open(f'{Storage.storage_name}.{Storage.storage_ext}', 'r') as file:

            for line in file:
                payload += line

        return payload

    @staticmethod
    def clear():
        print('clear')

        with open(f'{Storage.storage_name}.{Storage.storage_ext}', 'w') as file:
            file.write('')

    @staticmethod
    def create(name=''):
        print('create')

        if not name:
            storage_name = name

        with open(f'{Storage.storage_name}.{Storage.storage_ext}', 'w') as file:
            file.write('')

    @staticmethod
    def delete(name=''):
        print('delete')

        if not name:
            storage_name = name

        os.remove(f'{Storage.storage_name}.{Storage.storage_ext}')


class Managment(Storage):
    def __init__(self, payload=None, autocreate=False):
        self._payload = payload

        if autocreate:
            self.create()

    @property
    def payload(self):
        print('get payload')
        return self._payload

    @payload.setter
    def payload(self, payload=None):
        print('change payload')
        if sys.getsizeof(payload) == 0:
            raise ValueError('Payload must be more then 0 byte')
        elif sys.getsizeof(payload) > 100:
            raise ValueError('Payload must be less then 100 byte')

        self._payload = payload

        self.store(self._payload)