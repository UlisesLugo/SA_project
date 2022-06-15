import json
import models
from flask import Flask, request, json
from database_session import DatabaseSession
from movies.movie_queries import MovieQueries
from db_intializer import DBInitializer

app = Flask(__name__)
models.start_mappers()
DBInitializer.initialize_db()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/get_movies", methods=["GET"])
def get_movies():
    user_id = int(request.args.get("user_id"))
    rating = request.args.get("rating") in {"True", "true"}
    
    # logic to get user preference
    user = user_id

    # logic to get movies for user    
    movies = MovieQueries.get_movie_matches(user, rating)

    response = app.response_class(
        response=json.dumps(list(map(lambda x:x.to_dict(), movies))),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/register", methods=["POST"])
def register():
    args = request.json
    session = DatabaseSession()

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