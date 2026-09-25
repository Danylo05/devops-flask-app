from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.route("/about")
def about():
    return "About page + python page"

@app.route("/contact")
def about():
    return "email12348@gmail.com"
