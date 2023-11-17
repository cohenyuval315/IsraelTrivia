from flask_restful import Resource
from flask import jsonify, request, make_response
from .utils import parse_json
class Logout(Resource):
    def get(self):
        # Create a response to clear the 'username' cookie
        response = make_response("Logout successful")
        response.delete_cookie('username')
        return response