import json

def parse(path: str):
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

def getvaluekey(parsed_config: dict, value):
    return parsed_config[value]

def update(config_dict: dict, value, key):
    config_dict[value] = key
