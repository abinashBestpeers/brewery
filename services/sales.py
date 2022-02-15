from services import root_dir, nice_json
from flask import Flask
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("{}/database/sales.json".format(root_dir()), "r") as f:
    sales = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "sales": "/sales",
            "sales": "/sales/<name>"
        }
    })


@app.route("/sales", methods=['GET'])
def beer_list():
    return nice_json(sales)


@app.route("/sales/<name>", methods=['GET'])
def beer_record(name):
    if name not in sales:
        raise NotFound

    return nice_json(sales[name])

if __name__ == "__main__":
    app.run(port=5001, debug=True)