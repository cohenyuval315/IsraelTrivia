from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_bcrypt import Bcrypt
from .utils import generate_new_token


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

        # Check if the username already exists in the JSON file
        if data['username'] in users:
            return 'Username already exists.', 400

        password_token = generate_new_token() # todo change it

        salted_password = password_token + data['password']

        # Hash the password using Flask-Bcrypt
        password_hash = bcrypt.generate_password_hash(salted_password).decode('utf-8')

        # Create the user
        user = User(password_token=password_token, username=data['username'], password=password_hash)

        # Add the new user to the JSON file
        users[data['username']] = {'password_token': password_token, 'username': data['username'],
                                   'password_hash': password_hash, 'roles': user.role}
        # Todo add to DB
        return 'User registered successfully.', 201