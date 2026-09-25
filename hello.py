from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return "About page"

@app.route("/contact")
def about():
    return "email12348@gmail.com"