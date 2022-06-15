from movies.movie_preferences import MoviePreferences

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
        return MoviePreferences(self._user_preference, self._rating)
