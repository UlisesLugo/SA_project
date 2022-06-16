import models

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to build the User model object
class UserBuilder():
    def __init__(self):
        self._username = None
        self._rating = None
        self._preferences = None
        self._token = None
    
    def username(self, username):
        self._username = username
        return self

    def email(self, email):
        self._email = email
        return self

    def preferences(self, preferences):
        self._preferences = preferences
        return self

    def token(self, token):
        self._token = token
        return self
    
    def build(self):
        assert (self._username is not None   
                and self._email is not None 
                and self._preferences is not None
                and self._token is not None)
        return models.User(username=self._username,
                            email = self._email,
                            preferences = self._preferences,
                            token = self._token)