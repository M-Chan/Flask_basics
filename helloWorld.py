"""
basic flask application --> prints "Hello World!" in browser
use 'flask --app <filename> run' to run the program on a development server and then open it in a browser
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"