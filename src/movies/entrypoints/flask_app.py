import json
from flask import Flask, request, json
from movies import models

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/register", methods=["POST"])
def register():
    args = request.json

    username = args.get('username')
    email = args.get('email')
    preferences = args.get('preferences')

    if(username is None or email is None or preferences is None):
        return 'Username, email and preferences are required for registering', 400

    return "This is register :)", 200