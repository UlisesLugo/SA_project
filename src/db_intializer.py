import os
import csv
from datetime import datetime
from movies.movie_builder import MovieBuilder
from movies.movie_queries import MovieQueries
from users.user_queries import UserQueries
from users.user_builder import UserBuilder

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to initialize the DB
class DBInitializer():
    def initialize_db():
        if MovieQueries.is_empty():
            base_dir = os.path.dirname(os.path.realpath(__file__))
            with open(f"{base_dir}/movies/raw_data/movie_results.csv", "r") as movies_csv:
                csv_reader = csv.DictReader(movies_csv, skipinitialspace=True)
                movies = []
                for i, row in enumerate(csv_reader):
                    movie = (MovieBuilder()
                        .movie_id(i)
                        .preference_key(int(row["preference_key"]))
                        .movie_title(row["movie_title"])
                        .rating(float(row["rating"]))
                        .year(int(row["year"]))
                        .build())
                    movies.append(movie)
                MovieQueries.create_many(movies)
        
        if UserQueries.is_empty():
            user = (UserBuilder()
                .username("test_user")
                .email("hello@test.com")
                .preferences(["comedy","romantic","adventure"])
                .token("dummy_T0k3n")
                .build())
            UserQueries.create_one(user)