from flask_restful import Resource
from .utils import custom_login_required
from db import mongo
from flask import jsonify, request, make_response
from .utils import parse_json
from logger import logger
class UserProfile(Resource):
    """
    A class representing the User Profile resource.
    This resource is accessible to logged-in users.
    Methods:
        get(self): Handles GET requests for the User Profile.
    """

    def post(self):
        data = request.get_json()
        user_id = data['user_id']
        user = mongo.Users.get_user_by_id(user_id)
        return make_response(jsonify(parse_json(user)), 201)
    
    def put(self):
        logger.info("inside use update")
        data = request.get_json()
        user_id = data['user_id']
        level_id = data['level_id']
        level_index = data['level_index']
        score = data['score']
        new_data = {
            "level_id":level_id,
            "level_index":level_index,
            "score":score
        }
        logger.info(new_data)
        mongo.Users.update_user_progress(user_id, new_data)
        return make_response(jsonify(message="success!"), 201)