from movies.movie_matcher import MovieMatcher

class MovieQueries():
    def get_movie_matches(user, rating):
        return MovieMatcher.get_movie_preferences(user, rating)
