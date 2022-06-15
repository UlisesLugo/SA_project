import json
import models
from flask import Flask, request, json
from movies.movie_preferences import MoviePreferencesBuilder
from users.token_generator import generate_token
from users.user_builder import UserBuilder
from users.user_queries import UserQueries

app = Flask(__name__)
models.start_mappers()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/get_movies", methods=["GET"])
def get_movies():
    user_id = int(request.args.get("user_id"))
    rating = request.args.get("rating") in {"True", "true"}
    
    movie_prefs_builder = MoviePreferencesBuilder()
    movie_prefs = movie_prefs_builder.user_id(user_id).rating(rating).build()
    movies = movie_prefs.get_movies()
    
    response = app.response_class(
        response=json.dumps(list(map(lambda x:x.to_dict(), movies))),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/register", methods=["POST"])
def register():
    args = request.json

    username = args.get('username')
    email = args.get('email')
    preferences = args.get('preferences')

    if(username is None or email is None or preferences is None):
        return 'Username, email and preferences are required for registering', 400

    token = generate_token()
    user = (UserBuilder()
            .username(username)
            .email(email)
            .preferences([1,2,3])
            .token(token)
            .build())

    result = UserQueries.add_user(user)
    # Adding something to DB
    # session.add(models.Movie(movie_id=1, preference_key=3, movie_title="titanic", rating=7.9, year= 1990, create_time=datetime.now()))

    #  Querying to DB
    # for instance in session.query(models.Movie):
    #     print(instance.movie_id, instance.movie_title, instance.rating)

    if result :
        response = app.response_class(
            response=json.dumps(user.to_dict()),
            status=200,
            mimetype='application/json'
        )
    else:
        response = "Username duplicated, please change", 400

    return response