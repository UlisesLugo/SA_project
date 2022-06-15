from datetime import datetime
import models

class MovieBuilder():
    def __init__(self):
        self._movie_id = None
        self._preference_key = None
        self._movie_title = None
        self._rating = None
        self._year = None
        self._create_time = None

    def movie_id(self, movie_id):
        self._movie_id = movie_id
        return self

    def preference_key(self, preference_key):
        self._preference_key = preference_key
        return self

    def movie_title(self, movie_title):
        self._movie_title = movie_title
        return self

    def rating(self, rating):
        self._rating = rating
        return self

    def year(self, year):
        self._year = year
        return self

    def create_time(self, create_time):
        self._create_time = create_time
        return self

    def build(self):
        assert (self._movie_id is not None   
                and self._preference_key is not None 
                and self._movie_title is not None
                and self._rating is not None
                and self._year is not None)
        if self._create_time is None:
            self._create_time = datetime.now() 

        return models.Movie(
            movie_id=self._movie_id,
            preference_key=self._preference_key,
            movie_title=self._movie_title,
            rating=self._rating,
            year=self._year,
            create_time=self._create_time,
        )