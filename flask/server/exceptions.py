from logger import logger

class CustomExecption(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Default message for CustomException"
        super().__init__(message)
        logger.error(message)    

class CustomError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Default message for CustomError"
        super().__init__(message)
        logger.error(message)

