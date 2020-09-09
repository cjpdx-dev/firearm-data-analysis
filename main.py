from FDA_Dataset import FDA_Dataset

import json

from os import listdir
from os.path import isfile, join

from pathlib import Path


def main():

    json_dir = 'json/'
    json_file_names = get_json_file_names(json_dir)
    print(json_file_names)
    
    fda_dataset = FDA_Dataset(json_file_names)
    fda_dataset.parse_json_files()
    
    fda_dataset.print_year_data(1999)


def get_json_file_names(json_dir):
    '''
    Read in all json files within the given json directory and return a list of sorted .json file names
    Ignore (and log) any non-json files.

    :param json_dir: the name of the json directory
    :returns: a sorted list of .json file names
    '''

    file_names = [f for f in listdir(json_dir) if isfile(join('json/', f))]
    json_file_names = [f for f in file_names if Path(f).suffix=='.json']
    
    ignored_files = []
    for file_name in file_names:
        if file_name not in json_file_names:
            ignored_files.append(file_name)

    # FIXME: log this instead of printing it 
    print(str(len(ignored_files)) + " file(s) ignored: " + str(ignored_files))

    json_file_names.sort()

    return json_file_names


main()
