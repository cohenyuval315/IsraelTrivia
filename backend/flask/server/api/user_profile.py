from utils import custom_login_required

class UserProfile(Resource):
    """
    A class representing the User Profile resource.
    This resource is accessible to logged-in users.
    Methods:
        get(self): Handles GET requests for the User Profile.
    """

    @custom_login_required
    def get(self):
        """
        Handle GET requests for the User Profile.
        Returns:
            str: A message indicating access to the User Profile.
        """
        return "User Profile", 200