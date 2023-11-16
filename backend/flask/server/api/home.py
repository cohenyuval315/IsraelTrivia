from flask_restful import Resource
from flask import jsonify, request, make_response
from db import mongo


# Constants and paths
WELCOME_MSG = 'You have reached the server.'

# HTTP Response Messages
HTTP_SUCCESS_OK = 'OK'
HTTP_UNAUTHORIZED = 'Unauthorized'
HTTP_BAD_REQUEST = 'Bad Request'
HTTP_CREATED = 'Created'
HTTP_INTERNAL_SERVER_ERROR = 'Internal Server Error'


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
        lastest_metadata = mongo.Metadata.get_latest_metadata()
        return make_response(jsonify(message=lastest_metadata), 201)
    