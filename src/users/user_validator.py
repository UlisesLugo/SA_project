from movies.movie_matcher import MovieMatcher

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to validate the information of a User
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