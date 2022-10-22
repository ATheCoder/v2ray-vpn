import re

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def generate_json(path_to_template, replacement_dict):
    template = read_file(path_to_template)
    
    for key, value in replacement_dict.items():
        if isinstance(value, str):
            pattern = "\{\{ {} \}\}".replace('{}', key)
        elif isinstance(value, (int, float)):
            pattern = "\"\{\{ {} \}\}\"".replace('{}', key)
            
        else:
            raise Exception(f"Invalid type of {type(value)} in key {key}")
            
        template = re.sub(pattern, str(value), template)
    
    return template