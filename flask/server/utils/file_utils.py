import os
import json
from bleach import clean

class FileUtils:
    WRITE = "r+"
    JSONS_PATH = "ServerSide/server/Resources/jsons/"

    def is_valid(input):
        """
        A function that checks if the user's input is valid.
        :param input: The user input
        """
        # Implement your validation logic here
        # Return True if input is valid, False otherwise
        cleaned_input = clean(input)  # Sanitize
        return cleaned_input


    def validate_path_load_json(root,path):
        """
        A function that validates a file path, loads a JSON file, and returns the loaded object.
        :param extension: The file extension.
        :return: The loaded JSON object or None if the file doesn't exist.
        """

        # Define the path that you want to check. "/path/to/directory"
        path = os.getcwd() + root + path

        # Check if the file exists.
        if not os.path.exists(path):
            return None

        # Open the file to read only and return the loaded file.
        with open(path, 'r') as f:
            return json.load(f)