from flask_restful import Resource
from flask import jsonify, request, make_response


class Questions(Resource):
    def get(self):
        return make_response(jsonify(message=f"hello world"), 201)

    def post(self):
        data = request.get_json()
        return make_response(jsonify(message=f"hello world"), 201)

    

