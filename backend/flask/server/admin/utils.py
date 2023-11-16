from flask import request

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