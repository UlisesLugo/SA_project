from movies.movie_preferences_builder import MoviePreferencesBuilder

class MovieMatcher():
    def get_movie_preferences(user, rating):
        user_preference = user
        movie_prefs = MoviePreferencesBuilder().user_preference(user_preference).rating(rating).build()
        movies = movie_prefs.get_movies_list()
        return movies