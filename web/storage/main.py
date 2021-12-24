from storage import StorageWrap


if __name__ == '__main__':
    ip_addr = 'http://127.0.0.1:8000'

    sw = StorageWrap(ip_addr)
    sw.store('vk')
    print(sw.read())