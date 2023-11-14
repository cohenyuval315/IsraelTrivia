import logging
import os

def configure_logger() -> logging.Logger:
    LOG_LEVEL = os.environ.get("LOG_LEVEL",logging.INFO)
    
    logger = logging.getLogger("Logger")
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = configure_logger()

