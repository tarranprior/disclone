import json
import os, sys

'''
Function to return configuration data from './config.json'
'''
def load_configuration():
    if os.path.isfile("config.json"):
        with open("config.json") as json_file:
            data = json.load(json_file)
            return data
    else:
        sys.exit(f"Configuration file not found. Please add it and try again.")

'''
Function to update configuration data in './config.json'
'''
def update_configuration(key: str, value: str):
    if str(load_configuration()['configuration'][f'{key}']) != value:
        with open('config.json', 'r+') as json_file:
            data = json.load(json_file)
            data['configuration'][f'{key}'] = value
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
        return(data['configuration'][f'{key}'], value)
    return False