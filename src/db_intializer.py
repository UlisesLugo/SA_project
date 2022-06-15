import os
import csv
from datetime import datetime
from models import Movie
from movies.movie_queries import MovieQueries

class DBInitializer():
    def initialize_db():
        if MovieQueries.movies_empty():
            base_dir = os.path.dirname(os.path.realpath(__file__))
            with open(f"{base_dir}/movies/movie_results.csv", "r") as movies_csv:
                csv_reader = csv.DictReader(movies_csv, skipinitialspace=True)
                movies = []
                for i, row in enumerate(csv_reader):
                    movies.append(Movie(
                        movie_id=i,
                        preference_key=int(row["preference_key"]),
                        movie_title=row["movie_title"],
                        rating=float(row["rating"]),
                        year=int(row["year"]),
                        create_time=datetime.now(),
                    ))
                MovieQueries.add_movies(movies)