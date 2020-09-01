import json
import pandas as pd

def main():

    with open('json/fd1999.json', 'r') as json_file:
        
        data = json.load(json_file)

        print(data["monthly_data"][0]["jan"][0]["gun_bg_checks"])
        #pd_data = pd.read_json('json/fda1999.json')
        


main()