import json

def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
    return json_file
