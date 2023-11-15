from flask.blueprints import Blueprint
from flask_restful import Api
from .resource import HelloWorld


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(HelloWorld,"/hello")

