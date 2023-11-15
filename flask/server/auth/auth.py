from flask.blueprints import Blueprint
from flask_restful import Api
from register import Register
from login import Login
from logout import Logout

auth = Blueprint('auth', __name__)
api = Api(auth)

api.add_resource(Register,"/register")

api.add_resource(Login,"/login")

api.add_resource(Logout,"/logout")