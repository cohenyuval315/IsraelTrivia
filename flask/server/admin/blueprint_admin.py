from flask.blueprints import Blueprint
from flask_restful import Api
from dashboard import AdminDashboard

admin_bp = Blueprint('admin', __name__)
admin_api = Api(admin_bp)

admin_api.add_resource(AdminDashboard,"/")

admin_api.add_resource(AdminDashboard.Maintenance,"/Maintenance")