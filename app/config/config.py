import json
import os

APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__) or '.'))

with open(f'{APP_DIR}/config/config.json') as file:
    config = json.load(file)
