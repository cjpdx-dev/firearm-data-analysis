import json

def main():

    with open('json/gun_data.json', 'a+') as f:
        data = json.load(f)    

    return 0
