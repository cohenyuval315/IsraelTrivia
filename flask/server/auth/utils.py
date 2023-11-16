import secrets
from flask import request
from bleach import clean


TOKEN_LENGTH = 8  # Length of the secure token for user IDs

def is_valid(user_input):
    """
    A function that checks if the user's input is valid.
    :param user_input: The user input
    """
    # Implement your validation logic here
    # Return True if input is valid, False otherwise
    cleaned_input = clean(user_input)  # Sanitize
    return cleaned_input


def generate_new_token():
    """
    Generate a secure random token as the user ID
    Returns: The token generated
    """
    token = secrets.token_hex(8)  # Adjust the token length as needed
    return token


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        acct = basic_authentication()

        if acct:
            return func(*args, **kwargs)

        flask_restful.abort(401)

    return wrapper


def cache(f):
    @wraps(f)
    def cacher(*args, **kwargs):

        # caching stuff
        return cacher
