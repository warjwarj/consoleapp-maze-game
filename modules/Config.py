import json
import os

class InvalidConfigError(Exception):
    """ raised when the config  is not in the desired format. """

class Config:

    @staticmethod
    def read(pertinent_module):
        config = json.loads(open('./config.json').read())[pertinent_module]
        if pertinent_module == "Structure":
            if config["height"] % 2 and config["width"] % 2:
                return config
            else:
                print("config: Structure height needs to be an odd number")
                raise InvalidConfigError
        if pertinent_module == "Item":
            return config
        
