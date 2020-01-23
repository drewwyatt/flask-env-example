from flask import Flask, json, g, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

token = "123abc"


@app.route("/api/login", methods={"POST"})
def login():
    body = request.get_json()
    if "email" in body and "password" in body:
        return json_response({"token": token})
    return json_response({"error": "invalid credentials"}, 401)


@app.route("/api/foo", methods=["GET"])
def foo():
    return json_response({"hello": "world"})


@app.route("/api/bar", methods=["GET"])
def bar():
    authorization = request.headers.get("authorization", None)
    if authorization != token:
        return json_response({'error': 'no authorization token provied'}, 401)
    return json_response({"Wow": "you are authenticated"})


@app.errorhandler(404)
def page_not_found(error):
    return json_response({"error": "not found"}, 404)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})
