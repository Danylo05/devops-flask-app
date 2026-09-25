from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is another welcome"

@app.route("/about")
def about():
    return "About page"

@app.route("/contact")
def about():
    return "email12348@gmail.com"