from FDA_Year import FDA_Year
import json
from pathlib import Path
import traceback

class FDA_Dataset:

    def __init__(self, json_file_names):
    
        # self.fda_years = []
        self.fda_years = {}
        self.json_file_names = json_file_names
        
        try:
            self.parse_json_files()
        except Exception as e:
            print("An error occured when parsing JSON files: {}").format(e)

    def parse_json_files(self):

        # TODO: Add documentation here
        '''
        Add documentation
        '''

        for file_name in self.json_file_names:
            
            file_path = Path.cwd() / 'json/' / file_name

            try:
                with open(file_path, 'r') as json_file:
                    try:
                        json_data = json.load(json_file)
                    except:
                        raise JsonParsingError("An error occured when parsing the JSON file " + str(file_path))

            except FileNotFoundError as e:
                print("Couldn't open or read from file (%s)." % e)
                raise FileNotFoundError

            if json_data != None:
               
                try:
                    new_year = FDA_Year(json_data)
                    
                    if new_year.get_year_value() not in self.fda_years:
                        self.fda_years[new_year.get_year_value()] = new_year
                    else:
                        raise Exception("A duplicate year was detected")
                
                except Exception as e:
                    print("Could not create json year object: ", e)
                    
            else:
                raise Exception("JSON data was not created.")

    def set_year_range(self):

        pass

    def get_monthly_data(self):

        pass

    def check_exist(self):
        return "I exist"

    # a test method
    # def print_year_data(self, year):
        
        # for fda_year in self.fda_years:
            # if fda_year.get_year_value() == year:
                # print("\n" + "Data for " + str(fda_year.get_year_value()) + ":\n")
                # print(fda_year.get_year_data())
                # break

class JsonParsingError(Exception):
    pass