import os
from flask import Flask, json, g, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods={"GET"})
def index():
    return json_response({"message": "these are examples of some environment variables. (normally you would not print these!)",
                          "variables": {"FLASK_ENV": os.getenv("FLASK_ENV"),
                                        "MY_SECRET_VARIABLE": os.getenv("MY_SECRET_VARIABLE"),
                                        "SMTP_PASSWORD": os.getenv("SMTP_PASSWORD")
                                        }})


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})
