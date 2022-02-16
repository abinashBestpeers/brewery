from flask import Flask, make_response
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("beers.json", "r") as f:
    beers = json.load(f)

def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

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