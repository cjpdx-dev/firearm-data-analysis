import json

import pandas as pd

# TODO: Do we convert json_data into a pandas dataframe here or pass in a pd dataframe from FDA_Dataset.parse_json_files()?

class FDA_Year:

    def __init__(self, json_data):
        self.json_data = json_data

    def get_year_value(self):
        
        return self.json_data["year"]

    def get_year_data(self):

        return self.json_data