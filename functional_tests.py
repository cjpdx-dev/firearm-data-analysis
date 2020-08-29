import json
import load_data
import time
import unittest

class JsonTest(unittest.TestCase):

    def setUp(self):
        self.f = open('json/gun_data.json', 'a+')
        # Test if file is open
        self.data = json.load(self.f)
        # Test if json data is loaded
                 

    def tearDown(self):

        self.f.close()

if __name__ == '__main__':
	unittest.main(warnings='ignore')
