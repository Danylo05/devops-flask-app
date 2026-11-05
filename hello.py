import os
import json
import time
import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    decode_responses=True
)

CACHE_TTL = 600  # 10 minutes


def cache_get(key):
    data = r.get(key)
    if data is None:
        return None
    data = json.loads(data)
    if time.time() - data["time"] <= CACHE_TTL:
        return data["html"]
    return None


def cache_set(key, html):
    r.set(key, json.dumps({
        "html": html,
        "time": time.time()
    }))


@app.route("/")
def home():
    cached = cache_get("home")
    if cached is not None:
        return cached
    html = "Welcome!"
    cache_set("home", html)
    return html


@app.route("/about")
def about():
    cached = cache_get("about")
    if cached is not None:
        return cached
    html = "About page + python page"
    cache_set("about", html)
    return html


@app.route("/contact")
def contact():
    cached = cache_get("contact")
    if cached is not None:
        return cached
    html = "email12348@gmail.com"
    cache_set("contact", html)
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)