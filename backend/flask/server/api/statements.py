from flask_restful import Resource
from flask import jsonify, request, make_response
from db import mongo

class Statements(Resource):
    def post(self):
        mongo.Statements.get_level_statements(level_id=level_id)
        return make_response(jsonify(message=f"hello world"), 201)


