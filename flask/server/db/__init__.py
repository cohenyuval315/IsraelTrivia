from .db import MongoDB

def get_mongo_database(config):
    
    client = MongoClient(config.MONGO_API_URL)
    mongodb = client[config.MONGO_API_URL]
    return mongodb

