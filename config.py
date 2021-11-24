import os
import configparser

config_file = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
config = configparser.ConfigParser()
config.read(config_file)

FISHING_WIDTH = int(config['fishing']['width'])
FISHING_HEIGHT = int(config['fishing']['height'])