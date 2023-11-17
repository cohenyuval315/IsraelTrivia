from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_bcrypt import Bcrypt
from .utils import generate_new_token
from db import mongo
from .utils import parse_json
bcrypt = Bcrypt()


# Registration route class
class Register(Resource):
    """

    """

    def post(self):
        data = request.get_json()

        # Check if the required fields are provided in the request JSON
        if 'username' not in data or 'password' not in data:
            return 'Username and password are required.', 400

        # Check if the username already exists in the database
        if mongo.Users.is_username_exists(data['username']):
            return 'Username already exists.', 400

        password_token = generate_new_token()

        salted_password = password_token + data['password']

        # Hash the password using Flask-Bcrypt
        password_hash = bcrypt.generate_password_hash(salted_password).decode('utf-8')

        # Create the user
        mongo.Users.create_user(data['username'], password_hash, password_token)
        return 'User registered successfully.', 201
