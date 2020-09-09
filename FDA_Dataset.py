from FDA_Year import FDA_Year
import json
from pathlib import Path
import traceback

class FDA_Dataset:

    def __init__(self, json_file_names):
    
        self.fda_years = []
        self.json_file_names = json_file_names

    def parse_json_files(self):

        # TODO: Add documentation here
        '''
        Add documentation
        '''

        for file_name in self.json_file_names:
            file_path = Path.cwd() / 'json/' / file_name

            json_data = None

            try:
                
                with open(file_path, 'r') as json_file:
                    
                    try:
                        json_data = json.load(json_file)
                    except:
                        raise Exception("An error occured when parsing the JSON file " + str(file_path))

            except FileNotFoundError as e:
                print("Couldn't open or write to file (%s)." % e)

            if json_data != None:
                new_year = FDA_Year(json_data)
                self.fda_years.append(new_year)

    # a test method
    def print_year_data(self, year):
        
        for fda_year in self.fda_years:
            if fda_year.get_year_value() == year:
                print("\n" + "Data for " + str(fda_year.get_year_value()) + ":\n")
                print(fda_year.get_year_data())
                break






            
            

            