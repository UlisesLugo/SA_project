from array import array
from movies.movie_preferences_builder import MoviePreferencesBuilder
from functools import reduce

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to run the algorithm for calculating the preference key of the user
class MovieMatcher():
    categories = { "comedy": 1, "drama": 2, "sci-fi": 3, "romantic": 4, "adventure": 5}
    
    def _get_category_mapping(preferences):
        return [ MovieMatcher.categories.get(preference) for preference in preferences]
    
    def _compute_preference_number(user):
        user_prefs = user.preferences
        pref_num = reduce(lambda x,y: x*y, MovieMatcher._get_category_mapping(user_prefs)) % 5 + 1
        return pref_num

    def get_movie_preferences(user, rating):
        user_preference = MovieMatcher._compute_preference_number(user)
        movie_prefs = MoviePreferencesBuilder().user_preference(user_preference).rating(rating).build()
        return movie_prefs
