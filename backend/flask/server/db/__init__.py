from .db import MongoDB
import os
import exceptions

def get_db():
    MONGO_URL = os.environ.get("CONFIG_MONGODB_URL",None)
    MONGO_DATABASE_NAME = os.environ.get("CONFIG_MONGO_DATABASE_NAME",None)
    if not MONGO_URL:
        raise exceptions.ConfigurationNotFoundError("Mongo Connection String URL Configuration is not found")
    if not MONGO_DATABASE_NAME:
        raise exceptions.ConfigurationNotFoundError("Mongo Database Name Configuration is not found")
    mongo = MongoDB(MONGO_URL,MONGO_DATABASE_NAME)
    return mongo

