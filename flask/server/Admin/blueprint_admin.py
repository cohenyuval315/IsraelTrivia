from flask.blueprints import Blueprint
from flask_restful import Api
from dashboard import AdminDashboard

auth = Blueprint('admin', __name__)
api = Api(auth)

api.add_resource(AdminDashboard,"/admin")

api.add_resource(AdminDashboard.Maintenance,"/admin/Maintenance")