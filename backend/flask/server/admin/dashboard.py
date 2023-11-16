from flask_restful import Resource
from flask import jsonify, request, make_response

from .utils import custom_roles_required


class AdminDashboard(Resource):
    """
    A class representing the admin Dashboard resource.
    This resource is accessible to users with the 'admin' role.
    Methods:
        get(self): Handles GET requests for the admin Dashboard.
    """

#     @custom_roles_required('admin')
#     def get(self):
#         """
#         Handle GET requests for the admin Dashboard.
#         Returns:
#             str: A message indicating access to the admin Dashboard.
#         """
#         return "admin Dashboard", 200
#
    class Maintenance(Resource):
        """
        A template class for a maintenance endpoint.
        """

        def get(self):
            """
            Returns data for Endpoint 1.
            """
            # Get and return data for Maintenance
            pass

        def post(self):
            """
            Handles POST requests for Endpoint 1.
            """
            # Process the POST data and return response
            pass