from crud_interfaces import CreateObjectInterface, ReadObjectInterface
from movies.movie_matcher import MovieMatcher
from database_session import DatabaseSession
from models import Movie

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to query the Movie model
class MovieQueries(CreateObjectInterface, ReadObjectInterface):
    def get_movie_matches(user, rating):
        return MovieMatcher.get_movie_preferences(user, rating)

    def create_many(movies):
        session = DatabaseSession()
        for movie in movies:
            session.add(movie)
        session.commit()

    def is_empty():
        session = DatabaseSession()
        return session.query(Movie).first() is None