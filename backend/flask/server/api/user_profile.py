from flask_restful import Resource
from .utils import custom_login_required
from db import mongo
class UserProfile(Resource):
    """
    A class representing the User Profile resource.
    This resource is accessible to logged-in users.
    Methods:
        get(self): Handles GET requests for the User Profile.
    """

    @custom_login_required
    def get(self):
        mongo.Users.get_user_by_id(user_id)
        
    
    def update_progress(self):
        mongo.Users.update_user_progress(user_id,new_data)
        