import json

from os import listdir
from os.path import isfile, join

import pandas as pd
from pathlib import Path

def main():

    json_dir = 'json/'
    json_file_names = get_json_file_names(json_dir)
    print(json_file_names)

def get_json_file_names(json_dir):
    '''
    Read in all json files within the given json directory and return a list of sorted .json file names
    Ignore (and log) any non-json files.

    :param json_dir: the name of the json directory
    :returns: a sorted list of .json file names
    '''

    file_names = [f for f in listdir(json_dir) if isfile(join('json/', f))]
    json_file_names = [f for f in file_names if Path(f).suffix=='.json']
    
    ignored_file_names = []
    for fname in file_names:
        if fname not in json_file_names:
            ignored_file_names.append(fname)

    # log this instead of printing it    
    print(str(len(ignored_file_names)) + " file(s) ignored: " + str(ignored_file_names))

    json_file_names.sort()

    return json_file_names


main()