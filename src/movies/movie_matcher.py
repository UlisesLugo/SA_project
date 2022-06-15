from array import array
from movies.movie_preferences_builder import MoviePreferencesBuilder

class MovieMatcher():
    categories = { "comedy": 1, "drama": 2, "sci-fi": 3, "romantic": 4, "adventure": 5}

    def get_movie_preferences(user, rating):
        user_preference = user
        movie_prefs = MoviePreferencesBuilder().user_preference(user_preference).rating(rating).build()
        return movie_prefs

    def get_category_mapping(preferences):
        return [ MovieMatcher.categories.get(preference) for preference in preferences]
