from flask import Flask

app = Flask(__name__)
@app.route('/')

def say_hello():
    return '<p>Hello, World, I am a Flask app!</p>'