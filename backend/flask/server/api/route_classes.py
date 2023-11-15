import os
import json
import secrets

from flask import request, send_file, jsonify, make_response
from flask_restful import Resource
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta

from ServerSide.server.validation import is_valid, validate_path_load_json
from ServerSide.server.json_manipulation import load_users_from_json, load_roles_from_json ,save_users_to_json
from ServerSide.server.models import User, Role

# Constants and paths
WELCOME_MSG = 'You have reached the server.'
RESOURCES_PATH = "/path/to/resources"
JSONS_PATH = "/server/Resources/jsons/"

TOKEN_LENGTH = 8  # Length of the secure token for user IDs

# HTTP Response Messages
HTTP_SUCCESS_OK = 'OK'
HTTP_UNAUTHORIZED = 'Unauthorized'
HTTP_BAD_REQUEST = 'Bad Request'
HTTP_CREATED = 'Created'
HTTP_INTERNAL_SERVER_ERROR = 'Internal Server Error'

# Load users and roles from JSON files
users = load_users_from_json()
roles = load_roles_from_json()

bcrypt = Bcrypt()


# Function to generate a new user ID as a secure token
def generate_new_token():
    # Generate a secure random token as the user ID
    token = secrets.token_hex(8)  # Adjust the token length as needed

    return token


def delete_user(username):
    global users
    users = load_users_from_json()
    if username not in users:
        return "No such user"
    users.__delitem__(username)
    save_users_to_json(users)
    return "Operation successful"


def user_exists(username):
    return username in users


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
            if 'username' in request.cookies and request.cookies['username'] in users:
                user = users[request.cookies['username']]
                if 'roles' in user and role in user['roles']:
                    return func(*args, **kwargs)
            return "Unauthorized", 401

        return wrapper
    return decorator


class Home(Resource):
    """
    A class representing the homepage endpoint of the server.
    """
    # Test page, home() was here
    def get(self):
        """
        A method that returns a message when you reach the server.
        :return: A simple message.
        """
        return WELCOME_MSG, 200


# Registration route class
class Register(Resource):
    """

    """
    def post(self):
        global users
        users = load_users_from_json()
        data = request.get_json()

        # Check if the required fields are provided in the request JSON
        if 'username' not in data or 'password' not in data:
            return 'Username and password are required.', 400

        # Check if the username already exists in the JSON file
        if data['username'] in users:
            return 'Username already exists.', 400

        id = generate_new_token()

        salted_password = id + data['password']

        # Hash the password using Flask-Bcrypt
        password_hash = bcrypt.generate_password_hash(salted_password).decode('utf-8')

        # Create the user
        user = User(id=id, username=data['username'], password=password_hash)

        # Add the new user to the JSON file
        users[data['username']] = {'user_id': id, 'username': data['username'], 'password_hash': password_hash, 'roles': user.role}
        with open(os.getcwd() + JSONS_PATH + 'users.json', 'w') as users_file:
            json.dump(users, users_file, indent=4)
        return 'User registered successfully.', 201


class Login(Resource):
    """

    """
    def post(self):
        data = request.get_json()

        # Check if the required fields are provided in the request JSON
        if 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Username and password are required.'}), 400

        # Get username and password from the request
        unsanitized_username = data['username']
        unsanitized_password = data['password']

        # Sanitize and validate username and password
        username = is_valid(unsanitized_username)
        password = is_valid(unsanitized_password)

        if not username or not password:
            # If validation fails, return a general error message
            return jsonify({'error': 'Invalid username or password'}), 401

        # Check if the username exists in the user data
        if username in users:
            user = users[username]

            # Check if the provided password matches the stored hashed password
            if 'password_hash' in user:
                stored_password_hash = user['password_hash']
                # You should have stored the password securely hashed during user registration
                # Here, we'll use a simple hash comparison for demonstration purposes
                if bcrypt.check_password_hash(stored_password_hash, user['user_id'] + password):
                    # Successful login
                    response = make_response("Login successful")
                    # Set the 'username' cookie with a 2-hour expiration
                    expiration_time = datetime.now() + timedelta(hours=2)
                    response.set_cookie('username', username, expires=expiration_time)
                    return response

        # If login fails, return a general error message
        return jsonify({'error': 'Incorrect username or password'}), 401


class Logout(Resource):
    def get(self):
        # Create a response to clear the 'username' cookie
        response = make_response("Logout successful")
        response.delete_cookie('username')
        return response


class AdminDashboard(Resource):
    """
    A class representing the Admin Dashboard resource.
    This resource is accessible to users with the 'admin' role.
    Methods:
        get(self): Handles GET requests for the Admin Dashboard.
    """

    @custom_roles_required('admin')
    def get(self):
        """
        Handle GET requests for the Admin Dashboard.
        Returns:
            str: A message indicating access to the Admin Dashboard.
        """
        return "Admin Dashboard", 200

    class Maintenance(Resource):
        """
        A template class for a maintenance endpoint.
        """

        def get(self):
            """
            Returns data for Endpoint 1.
            """
            # Get and return data for Maintenance
            pass

        def post(self):
            """
            Handles POST requests for Endpoint 1.
            """
            # Process the POST data and return response
            pass


class UserProfile(Resource):
    """
    A class representing the User Profile resource.
    This resource is accessible to logged-in users.
    Methods:
        get(self): Handles GET requests for the User Profile.
    """

    @custom_login_required
    def get(self):
        """
        Handle GET requests for the User Profile.
        Returns:
            str: A message indicating access to the User Profile.
        """
        return "User Profile", 200


class Endpoint_1(Resource):
    """
    A class representing Endpoint 1 of the server.
    """

    def get(self):
        """
        Returns data for Endpoint 1.
        """
        # Get and return data for Endpoint 1
        user_input = request.form.get('user_input')
        # Validate and sanitize user_input here
        if not is_valid(user_input):
            return "Invalid input.", 400

        # Process the input
        pass

    def post(self):
        """
        Handles POST requests for Endpoint 1.
        """
        # Process the POST data and return response
        pass

    def put(self):
        """
        Handles PUT requests for Endpoint 1.
        """
        # Process the PUT data and return response
        pass

    def patch(self):
        """
        Handles PATCH requests for Endpoint 1.
        """
        # Process the PATCH data and return response
        pass

    def delete(self):
        """
        Handles DELETE requests for Endpoint 1.
        """
        # Process the DELETE request and return response
        pass


class Endpoint_2(Resource):
    """
    A class representing Endpoint 2 of the server.
    """

    def get(self):
        """
        Returns data for Endpoint 2.
        """
        # Get and return data for Endpoint 2
        pass

    # Implement POST, PUT, PATCH, and DELETE methods similarly


# Dictionary of endpoint classes to initiate URLs
class_dict = {"Home": Home, "Register": Register, "Login": Login, "Logout": Logout, "AdminDashboard": AdminDashboard,
              "AdminDashboard.Maintenance": AdminDashboard.Maintenance, "UserProfile": UserProfile,
              "Endpoint_1": Endpoint_1, "Endpoint_2": Endpoint_2}
