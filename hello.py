from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.route("/about")
def about():
    return "About page + python page"

@app.route("/contact")
def contact():
    return "email12348@gmail.com"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)