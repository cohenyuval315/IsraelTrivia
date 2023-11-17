from bson import json_util
import json

def parse_json(data):
    return json.loads(json_util.dumps(data))


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