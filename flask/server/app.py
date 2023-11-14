import os
from api import api_bp
from logger import logger
from flask import Flask
from flask_cors import CORS

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIR = "config"

def validate_configuration_file(config_filename):
    config_path = os.path.join(CURRENT_DIR,CONFIG_DIR,config_filename)
    if not os.path.exists(config_path):
        logger.error("Config File Not Found")
        raise FileNotFoundError(f"Configuration file is not found. Path: '{config_path}'")
    if not os.path.isfile(config_path):
        raise TypeError(f"This is not a file. Path: '{config_path}'")
    return config_path


def create_app(config_filename=None):
    """
    Creates and configures a Flask application instance.

    :return: The configured Flask app instance.
    """
    app = Flask(__name__)  

    if config_filename:
        CONFIG = validate_configuration_file(config_filename)
        app.config.from_file(CONFIG) # or app.config.from_object()
    
    app.config['SECRET_KEY'] = 'your_secret_key_here' 
    CORS(app)

    bp_efix = '/'
    app.register_blueprint(api_bp, url_prefix=bp_efix)

    return app


