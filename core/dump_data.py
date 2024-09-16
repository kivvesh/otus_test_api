import json


def dump_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=3)