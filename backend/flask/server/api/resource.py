from flask_restful import Resource
from flask import jsonify, request, make_response
from db import mongo

class HelloWorld(Resource):
    def get(self):
        mongo.Users.get_user_by_id()
        return make_response(jsonify(message=f"hello world"), 201)
    
    def post(self):
        data = request.get_json()
        return make_response(jsonify(message=f"hello world"), 201)

