import re

def parse_config(path: str):
    config_dict = {}

    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if ':' not in line:
            continue

        value, keys = line.split(':', 1)
        keys = keys.strip.rstrip(';')

        array_match = re.match(r'\((.*)\)')
        if array_match:
            keys = [key.strip() for key in array_match.group(1).split(',')]
        else:
            keys = keys.strip()

        config_dict[value] = keys

    return config_dict

def getvaluekey(parsed_config: dict, value: str):
    return parsed_config.get(value, None)
