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


# custom_login_required Decorator
def custom_login_required(func):
    """
    A decorator that checks if a user is logged in based on the presence of a 'username' cookie.
    If the user is logged in, it allows the decorated function to be executed.
    If the user is not logged in, it returns an "Unauthorized" response with a 401 status code.

    Args:
        func (function): The function to be decorated.
    Returns:
        function: The decorated function.
    """

    def wrapper(*args, **kwargs):
        """
        Inner function that performs the login check and role validation.
        Args:
            *args: Arbitrary positional arguments.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Any: The result of the decorated function or an "Unauthorized" response.
        """
        # Todo check if user logged in
        if 'username' in request.cookies and request.cookies['username'] in users:
            return func(*args, **kwargs)
        else:
            return "Unauthorized", 401

    return wrapper


# custom_roles_required Decorator
def custom_roles_required(role):
    """
    A decorator that checks if a user is logged in and has a specific role.
    It requires the user to have a 'username' cookie, be in the 'users' dictionary,
    and have the specified role in their 'roles' list.
    If the conditions are met, it allows the decorated function to be executed.
    If not, it returns an "Unauthorized" response with a 401 status code.
    Args:
        role (str): The role required to access the decorated function.
    Returns:
        function: The decorator function.
    """

    def decorator(func):
        """
        Inner decorator function that performs the role-based access check.
        Args:
            func (function): The function to be decorated.
        Returns:
            function: The decorated function.
        """

        def wrapper(*args, **kwargs):
            """
            Inner function that performs the role-based access check.
            Args:
                *args: Arbitrary positional arguments.
                **kwargs: Arbitrary keyword arguments.
            Returns:
                Any: The result of the decorated function or an "Unauthorized" response.
            """
            # todo check if user logged in and has the required role
            if 'username' in request.cookies and request.cookies['username'] in users:
                user = users[request.cookies['username']]
                if 'roles' in user and role in user['roles']:
                    return func(*args, **kwargs)
            return "Unauthorized", 401

        return wrapper

    return decorator


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
