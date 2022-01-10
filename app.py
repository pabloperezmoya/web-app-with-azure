from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "You'r in the root"

@app.route("/hello")
def hello():
    return "Hello"