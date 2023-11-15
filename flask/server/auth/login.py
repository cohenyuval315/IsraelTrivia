from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_bcrypt import Bcrypt
from utils import is_valid

bcrypt = Bcrypt()

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

        # Check if the username exists in the DB
        # Todo
        if username in users:
            user = users[username]

            # Check if the provided password matches the stored hashed password
            if 'password_hash' in user: # Todo check that its not null
                stored_password_hash = user['password_hash']
                if bcrypt.check_password_hash(stored_password_hash, user['password_token'] + password):
                    # Successful login
                    response = make_response("Login successful")
                    return response

        # If login fails, return a general error message
        return jsonify({'error': 'Incorrect username or password'}), 401