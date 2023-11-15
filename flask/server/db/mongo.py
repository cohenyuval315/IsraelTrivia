from datetime import datetime
from typing import Any
from uuid import uuid4  
from pymongo import MongoClient
import json
from logger import logger
from bson import ObjectId
import os 


def handle_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            logger.error(f"An exception occurred in {method.__name__}: {e}")

    return wrapper

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CollectionBase:
    def __init__(self,collection_name,db) -> None:
        self.collection_name = collection_name
        self.schema = self.load_schema(self.collection_name)
        # try:
        #     db.create_collection(self.collection_name,validator={"$jsonSchema": self.schema})
        # except Exception as e:
        #     raise Exception(f"error creating collection {self.collection_name} with validator. error: {e}")
        self.collection = db[self.collection_name]        
    
    @staticmethod
    def load_schema(collection_name):
        json_schema = None
        path = f"./db/schemas/{collection_name}.json"
        with open(path, 'r') as file:
            json_schema = json.load(file)
        if not json_schema:
            raise FileNotFoundError(f"{collection_name} schema is not found. path: {path}" ) 
        return json_schema
    
    def user_find_one(self,identity,collection_name ,filters=[]):
        user_filters = [{"_id": identity}]
        user_filters.extend(filters)
        ready_user_filters = {"$and":user_filters}
        result = self.db[collection_name].find_one(filter=ready_user_filters)
        return result



class Metadata(CollectionBase):
    def __init__(self, db) -> None:
        self.collection_name = "metadata"
        super().__init__(self.collection_name , db)

        self.default = {
            "version": 0,
            "date": datetime.now(),                
            "data": {
                "levels": [
                    {
                        "index": 1,
                        "level_name": "Beginner-1",
                        "num_questions": 5,
                        "question_difficulty_distribution": [100, 0, 0, 0, 0],
                        "min_score": 50
                    },
                    {
                        "index": 2,
                        "level_name": "Beginner-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [50, 50, 0, 0, 0],
                        "min_score": 50
                    },  
                    {
                        "index": 3,
                        "level_name": "Beginner-3",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 100, 0, 0, 0],
                        "min_score": 50
                    },                                                       
                    {
                        "index": 4,
                        "level_name": "Intermediate-1",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 50, 50, 0, 0],
                        "min_score": 50
                    },
                    {
                        "index": 5,
                        "level_name": "Intermediate-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 100, 0, 0],
                        "min_score": 50
                    },
                    {
                        "index": 6,
                        "level_name": "Intermediate-3",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 50, 50, 0],
                        "min_score": 300
                    },                                                
                    {
                        "index": 7,
                        "level_name": "Advanced-1",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 0, 100, 0],
                        "min_score": 350
                    },
                    {
                        "index": 8,
                        "level_name": "Advanced-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 0, 50, 50],
                        "min_score": 400
                    },
                    {
                        "index": 9,
                        "level_name": "Advanced-3",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 0, 0, 100],
                        "min_score": 450
                    }                                                                          
                ],
                "questions_difficulties": [
                    {"weight":10,"time_in_sec":10},
                    {"weight":20,"time_in_sec":10},
                    {"weight":30,"time_in_sec":10},
                    {"weight":40,"time_in_sec":10},
                    {"weight":50,"time_in_sec":10}
                ],
                "categories": [
                    {"category_id": ObjectId(), "title": "Other"},
                    {"category_id": ObjectId(), "title": "History"},
                    {"category_id": ObjectId(), "title": "Politics"},
                    {"category_id": ObjectId(), "title": "Geography"},
                    {"category_id": ObjectId(), "title": "Sports"},
                    {"category_id": ObjectId(), "title": "Music"},
                    {"category_id": ObjectId(), "title": "Art"}
                ],
                "question_types": [
                    {"question_type_id": ObjectId(), "title": "True Or False"},
                    {"question_type_id": ObjectId(), "title": "Four Options"},
                    {"question_type_id": ObjectId(), "title": "Two Options"}
                ],
                "supported_languages": [
                    {"language_id": ObjectId(), "language": "English", "symbol":"en"}
                ],
                "application_settings": [
                    {"setting_id": ObjectId(), "title": "Theme", "default_value": "white", "description": "application color theme"}
                ]
            }
        } 
        

    def insert(self, metadata_obj):
        latest_version_document = self.get_latest_metadata()
        latest_version = latest_version_document[0]['version'] if latest_version_document.count() > 0 else 0
        metadata_obj['version'] = latest_version + 1
        res = self.collection.insert_one(metadata_obj)
        return res

    
    def get_latest_metadata(self):
        latest_document = self.collection.find({}).sort('datetime', -1).limit(1)
        return latest_document
    
    def get_roles_and_permissions():
        pass

class Users(CollectionBase):
    def __init__(self, db) -> None:
        self.collection_name = "users"
        super().__init__(self.collection_name , db)

    def get_user_by_id(self):
        logger.info("get_user_by")

class Questions(CollectionBase):
    def __init__(self, db) -> None:
        self.collection_name = "questions"
        super().__init__(self.collection_name , db)

    def create_new_question(self):
        pass

    def get_random_question_by_difficulty(self,difficulty):
        pass

    def get_batch_random_questions(self,num_of_questions):
        pass

class MongoDB(metaclass=Singleton):
    
    def __init__(self,mongo_url,database_name) -> None:
        self.client = MongoClient(mongo_url)
        self.db = self.client[f"{database_name}"]
        self.metadata = Metadata(self.db)
        self.users = Users(self.db)
        self.questions = Questions(self.db)
    
    @property
    def Users(self):
        return self.users
    
    @property
    def Metadata(self):
        return self.metadata
    
    @property
    def Questions(self):
        return self.questions
        
    def close_connection(self):
        self.client.close()
    



    def create_metadata():
        sc = {
        "metadata":"",
        "version":"0.0.1",
        "datetime":"",
        "data":{
                    "levels":[
                        {
                            "index":1,
                            "level_name":"",
                            "num_questions":"",
                            "question_difficulty_distributiin":[],
                            "min_score":""
                        }
                    ,],
                    "questions_difficulty_weights":[10,20,30,40,50],
                    "categories":[
                        {
                            "category_id":ObjectId,
                            "title":""
                        }
                    ],
                    "question_types":[
                        {
                        "question_type_id":ObjectId,
                        "title":""
                        }
                    ],
                    "supported_languages":[
                        {
                            "language_id":ObjectId,
                            "language":""
                        }
                    ],
                    "application_settings":[
                        {
                            "setting_id":ObjectId,
                            "title":"",
                            "default_value":"",
                            "describption":""
                        }
                    ],
                    "roles":[
                        {
                            "role_id":ObjectId,
                            "role_title":"",
                            "roles_ids":["role_id"],
                            "role_permissions":[]
                        }
                    ],
                    "permission":[
                        {
                            "permission_id":ObjectId,
                            "permission":"delete level",
                        }
                    ]
            }
        }

    def create_user(self,username,password,password_token,):
        user_schema = {
            "_id":ObjectId(),
            "username":username,
            "password":password,
            "password_token":password_token,
            "current_level_index":0,
            "levels_highscores":[],            
            "settings":[], # empty = use default
            "role_id":""
        }

    def das(self):
        pass




# schema = {
#     "users": {
#         "_id": ObjectId("question_id"),
#         "username":"",
#         "password":"",
#         "password_token":"",
#         "current_level_index"
#         "levels_highscores":[
#             {
#                 "level_index",
#                 "highscore",
#                 "date",
#             }
#         ],
#         "settings":[
#             {
#                 "setting_id":"",
#                 "value":""
#             }
#         ],
#     },
    
#     "questions":{
#         "question_id":"",
#         "question": {
#             "en":"",
#             "es":""
#         },
#         "question_type_id":""
#         "category_id":"",
#         "difficulty":"",
#         "options":{ # at least 1 option en/ es / whatever, which is array of options, Or an Empty json 
#             "en": ["answer1, asnwer2 , asnwer3"],
#             "es": [] 
#         },
#         "right_answer_index": 0,
#         "solution":"string",
#         "referenaces", [], # list of links
#     },

#     "metadata":{
#         "levels":[
#             {
#                 "index":1
#                 "level_name":""
#                 "num_questions":""
#                 "question_difficulty_distributiin":[],
#                 "min_score":""
#             }
#         ,],
#         "difficulty_weights":[10,20,30,40,50],
#         "categories":[{
#             "category_id",
#             "title"
#         }],
#         "question_types":[{
#             "question_type_id"
#             "title"
#         }],
#         "supported_languages":[
#             {
#                 "language_id"
#                 "language"
#             }
#         ],
#         "application_settings":[
#             {
#                 "setting_id":
#                 "title"
#                 "default_value",
#                 "describption"
#             }
#         ],
#         "roles":[
#             {
#                 "role_id":0,
#                 "role_title",
#                 "role_level":1
#             }
#         ]
#     }
# }