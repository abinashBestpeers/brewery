from services import root_dir, nice_json
from flask import Flask
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("{}/database/accounts.json".format(root_dir()), "r") as f:
    accounts = json.load(f)

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
def beer_list():
    return nice_json(accounts)


@app.route("/accounts/<name>", methods=['GET'])
def beer_record(name):
    if name not in accounts:
        raise NotFound

    return nice_json(accounts[name])

if __name__ == "__main__":
    app.run(port=5002, debug=True)