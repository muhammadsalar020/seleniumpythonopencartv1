import configparser
import os

config = configparser.RawConfigParser()

# Get project root directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Full path to config.ini
config_path = os.path.join(base_dir, "configurations", "config.ini")

config.read(config_path)

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo', 'baseURL')

    @staticmethod
    def getUseremail():
        return config.get('commonInfo', 'email')

    @staticmethod
    def getPassword():
        return config.get('commonInfo', 'password')

#Testing above methods - optional Code
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())

