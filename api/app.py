from crypt import methods
from flask import Flask, make_response
from werkzeug.exceptions import NotFound
import requests

app = Flask(__name__)

@app.route("/sales", methods=["GET"])
def sales():
    url = "http://sales:5001/sales"
    reply = requests.get(url)
    reply = reply.json()

    return reply

@app.route("/sales/<name>", methods=["GET"])
def sales_records(name):
    url = "http://sales:5001/sales"
    reply = requests.get(f"{url}/{name}")
    reply = reply.json()

    return reply

@app.route("/accounts", methods=["GET"])
def accounts():
    url = "http://accounting:5002/accounts"
    reply = requests.get(url)
    reply = reply.json()

    return reply

@app.route("/accounts/<name>", methods=["GET"])
def accounts_records(name):
    url = "http://accounting:5002/accounts"
    reply = requests.get(f"{url}/{name}")
    reply = reply.json()

    return reply

@app.route("/warehouse/beers", methods=["GET"])
def beers():
    url = "http://warehouse:5003/warehouse/beers"
    reply = requests.get(url)
    reply = reply.json()

    return reply

@app.route("/warehouse/beers/<name>", methods=["GET"])
def beers_records(name):
    url = "http://warehouse:5003/warehouse/beers"
    reply = requests.get(f"{url}/{name}")
    reply = reply.json()

    return reply

if __name__ == "__main__":
    app.run(port=5000, debug=True)