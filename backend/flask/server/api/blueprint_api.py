from flask.blueprints import Blueprint
from flask_restful import Api
from .resource import HelloWorld
from .questions import Questions
from .user_profile import UserProfile

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(HelloWorld, "/hello")

api.add_resource(Questions, "/questions")

api.add_resource(UserProfile, "/profile")
