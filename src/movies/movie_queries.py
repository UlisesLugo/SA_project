from movies.movie_matcher import MovieMatcher
from database_session import DatabaseSession
from models import Movie
class MovieQueries():
    def get_movie_matches(user, rating):
        return MovieMatcher.get_movie_preferences(user, rating)

    def add_movies(movies):
        session = DatabaseSession()
        for movie in movies:
            session.add(movie)
        session.commit()

    def movies_empty():
        session = DatabaseSession()
        return session.query(Movie).first() is None