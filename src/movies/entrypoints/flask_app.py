import json
from flask import Flask, request, json
from movies import models
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
models.start_mappers()

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        models.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()

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

    # Adding something to DB
    # session.add(models.Movie(movie_id=1, preference_key=3, movie_title="titanic", rating=7.9, year= 1990, create_time=datetime.now()))

    #  Querying to DB
    # for instance in session.query(models.Movie):
    #     print(instance.movie_id, instance.movie_title, instance.rating)

    return "This is register :)", 200