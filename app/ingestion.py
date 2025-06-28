# load json file 

import json


def clean_data( data  ) :
    if isinstance( data, str ):
        return data.replace("\n"," ").replace("\t"," ").replace("\r"," ")
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, dict):
        return { clean_data(key) : clean_data(value) for key, value in data.items()}
    
    
def load_data_annexe1(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_data_annexe2(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file, strict = False)
    
    return clean_data(data)

