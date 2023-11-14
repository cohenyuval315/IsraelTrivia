from ServerSide.server.route_classes import class_dict


def create_dict(endpoints_dict):
    """
    A function that receives a path to the configuration file and returns the resource dictionary.
    :param endpoints_dict: The path to the configuration file.
    :return: The resource dictionary with all the endpoints.
    """

    r_dict = {}  # The dict to store the classes and the endpoints.

    # Check if the length is the same.
    if len(endpoints_dict) != len(class_dict):
        return None

    # Iterate over all the endpoints.
    for endpoint in endpoints_dict:
        if endpoint in class_dict:
            r_dict[class_dict[endpoint]] = endpoints_dict[endpoint]["controller"]  # Add to the dictionary.
        else:
            return None

    return r_dict


def initiate_resources(app, resource_dict):
    """
    A function that
    :param resource_dict: The dictionary of all the classes and routes.
    :param app:
    """
    for route_class, url in resource_dict.items():
        # Initiate all resources.
        app.add_url_rule('/' + url, view_func=route_class.as_view(url))


# api.com
def initialize_routes(api, resource_dict):
    """
    A function that
    :param resource_dict: The dictionary of all the classes and routes.
    :param api:
    """
    for route_class, url in resource_dict.items():
        # Initialize all routes.
        api.add_resource(route_class, '/' + url)
