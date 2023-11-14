from datetime import datetime
from uuid import uuid4  
from pymongo import MongoClient
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class MongoDB(metaclass=Singleton):
    
    def __init__(self,mongo_url,database_name) -> None:
        self.client = MongoClient(mongo_url)
        self.db = self.client(database_name)

    def user_find_one(self,identity,collection_name ,filters=[]):
        user_filters = [{"username": identity}]
        user_filters.extend(filters)
        ready_user_filters = {"$and":user_filters}
        result = self.db[collection_name].find_one(filter=ready_user_filters)
        return result
