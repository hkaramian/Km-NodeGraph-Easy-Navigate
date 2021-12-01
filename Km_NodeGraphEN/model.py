""" data managment - store data in file"""


import json
import os


class Settings():
    @staticmethod
    def Load():
        pluginPath = os.path.dirname(__file__)
        with open(pluginPath+'/settings.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def Save(settingsData):
        pluginPath = os.path.dirname(__file__)
        with open(pluginPath+'/settings.json', 'w') as outfile:
            json.dump(settingsData, outfile)
