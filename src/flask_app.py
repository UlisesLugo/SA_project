import json
from models import Models
from flask import Flask, request, json
from users.token_generator import generate_token
from users.user_builder import UserBuilder
from users.user_queries import UserQueries
from users.user_validator import UserValidator
from movies.movie_queries import MovieQueries
from db_intializer import DBInitializer

app = Flask(__name__)
Models.start_mappers()
DBInitializer.initialize_db()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route("/get_movies", methods=["GET"])
def get_movies():
    user_id = int(request.args.get("user_id"))
    rating = not request.args.get("rating") in {"False", "false"}
    
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

    username = args.get('username')
    email = args.get('email')
    preferences = args.get('preferences')

    isValidUser, errorUser = UserValidator.validate(username, email, preferences)
    if not isValidUser:
        return errorUser, 400

    token = generate_token()
    user = (UserBuilder()
            .username(username)
            .email(email)
            .preferences(preferences)
            .token(token)
            .build())

    print(user)
    result, errorMessage = UserQueries.add_user(user)

    if result :
        response = app.response_class(
            response=json.dumps(user.to_dict()),
            status=200,
            mimetype='application/json'
        )
    else:
        response = errorMessage, 400

    return response