from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my system, Please login.'

@app.route('/login/<name>')
def login(name):
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
        if name in config_data:
            return "Access Granted"
        else:
            return "Access Denied" 
    except FileNotFoundError:
        return "Error: Config file missing."
    # return f'Hello, {name}! You have successfully logged in.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)