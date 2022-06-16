from database_session import DatabaseSession
from models import Movie

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to build the MoviePreference query object
class MoviePreferencesBuilder():
    def __init__(self):
        self._user_preference = None
        self._rating = None
    
    def user_preference(self, user_preference):
        self._user_preference = user_preference
        return self

    def rating(self, rating):
        self._rating = rating
        return self
    
    def build(self):
        assert self._user_preference is not None and self._rating is not None
        query = DatabaseSession().query(Movie).filter_by(preference_key=self._user_preference)
        if self._rating:
            query = query.order_by(Movie.rating.desc())
        else:
            query = query.order_by(Movie.rating)
        return query.limit(10).all()
