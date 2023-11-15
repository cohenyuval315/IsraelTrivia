import logging
import os

LOGGER_NAME = "Logger"

def configure_logger() -> logging.Logger:
    LOG_LEVEL = os.environ.get("LOG_LEVEL",logging.INFO)
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = configure_logger()

