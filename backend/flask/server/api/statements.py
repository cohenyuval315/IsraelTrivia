from flask_restful import Resource
from flask import jsonify, request, make_response
from db import mongo
from .utils import parse_json
class Statements(Resource):
    def post(self):
        data = request.get_json()
        level_id = data['level_id']
        statements = mongo.Statements.get_level_statements(level_id=level_id)
        return make_response(jsonify(parse_json(statements)), 201)


