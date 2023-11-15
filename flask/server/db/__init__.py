from .mongo import MongoDB
import os
import exceptions
from logger import logger

def init_db():
    MONGO_URL = os.environ.get("CONFIG_MONGODB_URI",None)
    MONGO_DATABASE_NAME = os.environ.get("CONFIG_MONGO_DATABASE_NAME",None)
    if not MONGO_URL:
        raise exceptions.ConfigurationNotFoundError("Mongo Connection String URL Configuration is not found")
    if not MONGO_DATABASE_NAME:
        raise exceptions.ConfigurationNotFoundError("Mongo Database Name Configuration is not found")
    try:
        mongo = MongoDB(MONGO_URL,MONGO_DATABASE_NAME)    
        return mongo
    except Exception as e:
        logger.error(e)
        raise Exception(f"URI: {MONGO_URL} ,database name: {MONGO_DATABASE_NAME}")
    
logger.info("Initializing Mongodb ...")
mongo = init_db()