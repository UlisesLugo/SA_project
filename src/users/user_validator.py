from movies.movie_matcher import MovieMatcher

class UserValidator():
    def validate(username, email, preferences):

        if username is None:
            return 'username is required for registering', 400

        if email is None:
            return "email is required for registering", 400

        if preferences is None:
            return "preferences are required for registering", 400
        
        if not isinstance(preferences, list) or len(preferences) != 3:
            return False, "preferences has to be a list of 3 elements"
        
        for preference in preferences:
            if MovieMatcher.categories.get(preference) is None:
                return False, preference + " is not a valid preference"
        
        return True, ""