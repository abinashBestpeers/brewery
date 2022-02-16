from flask import Flask, make_response
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("accounts.json", "r") as f:
    accounts = json.load(f)

def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "beers": "/accounts",
            "beer": "/accounts/<name>"
        }
    })


@app.route("/accounts", methods=['GET'])
def account_list():
    return nice_json(accounts)


@app.route("/accounts/<name>", methods=['GET'])
def account_record(name):
    if name not in accounts:
        raise NotFound

    return nice_json(accounts[name])

if __name__ == "__main__":
    app.run(port=5002, debug=True)