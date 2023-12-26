# Filename: app.py
from flask import Flask  # import Flask in Python

app = Flask(__name__)  # create an instance of a Flask app


@app.route('/')  # route called by user
def index():  # function called by '/' route
    return 'Hello World! This App is built using Flask.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  # starts the web app at port 8000
