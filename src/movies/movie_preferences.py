from models import Movie
from database_session import DatabaseSession

class MoviePreferences():
    def __init__(self, user_id, rating):
        self.user_id = user_id
        self.rating = rating
    
    def get_movies_list(self):
        query = DatabaseSession().query(Movie).filter_by(preference_key=self.user_id)
        if self.rating:
            query = query.order_by(Movie.rating.desc())
        else:
            query = query.order_by(Movie.rating)
        return query.limit(10).all()

class MoviePreferencesBuilder():
    def __init__(self):
        self._user_preference = None
        self._rating = None
    
    def user_preference(self, user_preference):
        self._user_preference = user_preference
        return self

    def rating(self, rating):
        self._rating = True if rating is None else rating
        return self
    
    def build(self):
        assert self._user_id is not None and self._rating is not None
        return MoviePreferences(self._user_id, self._rating)