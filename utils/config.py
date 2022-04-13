import os
import sys
import json

HERE = here = os.path.dirname(os.path.realpath(__file__))

class BaseConfig():
    
    def __init__(self):
        with open(os.path.join(HERE, "..", "config", "config.json"), mode="r") as config_file:
            self.config = json.load(config_file)
    
    def get_config(self, *args):
        result = self.config
        for arg in args:
            result = result.get(arg, "")
        return result