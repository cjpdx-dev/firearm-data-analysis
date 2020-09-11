import json

import pandas as pd

# TODO: Do we convert json_data into a pandas dataframe here or pass in a pd dataframe from FDA_Dataset.parse_json_files()?

class FDA_Year:

    def __init__(self, json_data):
        
        self.json_data = json_data
        self.year_value = str(self.json_data["year_value"])
        
    def get_year_value(self):
        
        return self.year_value

    def get_all_data(self):

        return self.json_data

    def get_monthly_data(self):

        pass

