import json
import yaml
import pathlib


class Storage:
    def get_value(self, key):
        raise NotImplementedError


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as fd:
            data = json.load(fd)
            return data.get(key)


class YamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as fd:
            data = yaml.load(fd, Loader=yaml.FullLoader)
            return data.get(key)


class Service:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':
    storage_json = JSONStorage(pathlib.Path() / 'data.json')
    service_one = Service(storage_json)
    print(service_one.get('name'))

    storage_yaml = YamlStorage(pathlib.Path() / 'data.yaml')
    service_two = Service(storage_yaml)
    print(service_two.get('name'))
