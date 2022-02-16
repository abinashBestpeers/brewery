from flask import Flask, make_response
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("sales.json", "r") as f:
    sales = json.load(f)

def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

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
def sales_list():
    return nice_json(sales)


@app.route("/sales/<name>", methods=['GET'])
def sales_record(name):
    if name not in sales:
        raise NotFound

    return nice_json(sales[name])

if __name__ == "__main__":
    app.run(port=5001, debug=True)