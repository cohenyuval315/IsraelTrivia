from flask.blueprints import Blueprint
from flask_restful import Api
from register import Register
from login import Login
from logout import Logout

auth_bp = Blueprint('auth', __name__)
auth_api = Api(auth_bp)

auth_api.add_resource(Register,"/register")

auth_api.add_resource(Login,"/login")

auth_api.add_resource(Logout,"/logout")