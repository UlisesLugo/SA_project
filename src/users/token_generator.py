import random
import string

TOKEN_LENGTH = 12

# This class applies the Single Responsibility Principle (SRP)
# Its only objective is to generate the unique token for the user
class TokenGenerator:
    def generate_token():
        # Random string of length TOKEN_LENGTH with letters, digits, and symbols
        characters = string.ascii_letters + string.digits + string.punctuation
        token = ''.join(random.choice(characters) for i in range(TOKEN_LENGTH))
        return token