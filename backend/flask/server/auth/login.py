from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_bcrypt import Bcrypt
from .utils import is_valid
from db import mongo
from .utils import parse_json

bcrypt = Bcrypt()


online_users = []


def connect_user(user):
    """

    """
    online_users.append(user)


def disconnect_user(user):
    """

    """
    online_users.remove(user)


def is_user_online(user):
    """

    """
    if user in online_users:
        return True
    return False


class Login(Resource):
    """

    """
    def post(self):
        """

        """
        data = request.get_json()

        # Check if the required fields are provided in the request JSON
        if 'username' not in data or 'password' not in data:
            return make_response(jsonify({'message': 'Username and password are required.'}), 400)

        # Get username and password from the request
        unsanitized_username = data['username']
        unsanitized_password = data['password']

        # Sanitize and validate username and password
        username = is_valid(unsanitized_username)
        password = is_valid(unsanitized_password)

        if not username or not password:
            # If validation fails, return a general error message
            return make_response(jsonify({'error': 'Invalid username or password'}), 401)

        # Check if the username exists in the DB
        if mongo.Users.is_username_exists(data['username']):

            if is_user_online(username):
                return make_response(jsonify({'error': 'Already logged in'}), 401)

            # Check if the provided password matches the stored hashed password
            stored_password_hash = mongo.Users.get_password_by_username(username)
            stored_token = mongo.Users.get_token_by_username(username)
            if bcrypt.check_password_hash(stored_password_hash, stored_token + password):
                # Successful login

                connect_user(username)  # Add user to the online users array
                user = mongo.Users.get_user_by_username(username)
                user_id = user['user_id']
                return make_response(jsonify(parse_json(user_id)), 200)




        # If login fails, return a general error message
        return make_response(jsonify({'error': 'Incorrect username or password'}), 401)


class Logout(Resource):
    """

    """
    def get(self):
        """

        """
        data = request.get_json()

        # Check if the required fields are provided in the request JSON
        if 'username' not in data:
            return make_response(jsonify({'message': 'Username and password are required.'}), 400)

        # Get username and password from the request
        unsanitized_username = data['username']

        # Sanitize and validate username and password
        username = is_valid(unsanitized_username)

        if not username:
            # If validation fails, return a general error message
            return make_response(jsonify({'error': 'Invalid username or password'}), 401)

        # Remove user from logged in array.
        if is_user_online(username):
            disconnect_user(username)
        else:
            return make_response(jsonify({'error': 'User is not logged in'}), 401)

        response = make_response("Logout successful")
        return response
