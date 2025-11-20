from flask import Flask
import json
import os
import logging

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
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            logging.debug("Config file found")
        if name in config_data:
            logging.info(f"Name {name} is granted access")
            return "Access Granted"
        else:
            logging.warning(f"Name {name} is not granted access")
            return "Access Denied" 
    except FileNotFoundError:
        logging.critical("Config file does not exist!")
        return "Error: Config file missing."
    # return f'Hello, {name}! You have successfully logged in.'

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST_IP'), port=80)