from flask.blueprints import Blueprint
from flask_restful import Api
from .statements import Statements
from .user_profile import UserProfile
from .home import Home

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Statements, "/statements")
api.add_resource(UserProfile, "/user")
api.add_resource(Home, "/appdata")

