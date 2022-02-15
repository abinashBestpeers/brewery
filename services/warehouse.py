from services import root_dir, nice_json
from flask import Flask
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("{}/database/beers.json".format(root_dir()), "r") as f:
    beers = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "beers": "/warehouse/beers",
            "beer": "/warehouse/beers/<name>"
        }
    })


@app.route("/warehouse/beers", methods=['GET'])
def beer_list():
    return nice_json(beers)


@app.route("/warehouse/beer/<name>", methods=['GET'])
def beer_record(name):
    if name not in beers:
        raise NotFound

    return nice_json(beers[name])

if __name__ == "__main__":
    app.run(port=5003, debug=True)