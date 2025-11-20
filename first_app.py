from flask import Flask
import json
import os
import logging
from printColors import printGreen, printRed, printBlack
import json

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to the console
    ],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@app.route('/')
def welcome():
    return 'Welcome to my system, Please login.'

@app.route('/login/<name>')
def login(name):
    if name in allowed_users:
        logging.info(f"Name {name} is granted access")
        response = printGreen("Access Granted")
    else:
        logging.warning(f"Name {name} is not granted access")
        response = printRed("Access Denied")
    return response

@app.route('/addName/<name>')
def addName(name):
    response = printGreen(f"Name {name} added successfully")
    allowed_users.add(name)
    with open('config.json', 'w') as allowed_users_file:
        json.dump(list(allowed_users), allowed_users_file)
    return response

try:
    with open('config.json', 'r') as config_file:
            allowed_users = json.load(config_file)
            for name in allowed_users:
                logging.info(f"Allowed user from config: {name}")
            allowed_users = set(allowed_users)
            logging.info(f"Config file {config_file} found")            
except FileNotFoundError:
        logging.critical("Config file does not exist!")
        printBlack("Error: Config file missing.")
        

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST_IP'), port=80)