from datetime import datetime
from typing import Any
import exceptions
from uuid import uuid4  
from pymongo import MongoClient
import json
from logger import logger
from pymongo.collection import ReturnDocument
from bson import ObjectId
import os 
import random

def handle_exceptions(method):
    def wrapper(*args, **kwargs):
        try:
            res = method(*args, **kwargs)
            logger.debug(f"response of {method.__name__}:")
            logger.debug(res)
            return res
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
    
    def drop(self):
        self.collection.drop()
    

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
                        "level_id":ObjectId(),
                        "index": 1,
                        "level_name": "Beginner-1",
                        "num_questions": 5,
                        "question_difficulty_distribution": [100, 0, 0, 0, 0],
                        "min_score": 50
                    },
                    {
                        "level_id":ObjectId(),
                        "index": 2,
                        "level_name": "Beginner-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [50, 50, 0, 0, 0],
                        "min_score": 50
                    },  
                    {
                        "level_id":ObjectId(),
                        "index": 3,
                        "level_name": "Beginner-3",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 100, 0, 0, 0],
                        "min_score": 50
                    },                                                       
                    {
                        "level_id":ObjectId(),
                        "index": 4,
                        "level_name": "Intermediate-1",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 50, 50, 0, 0],
                        "min_score": 50
                    },
                    {
                        "level_id":ObjectId(),
                        "index": 5,
                        "level_name": "Intermediate-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 100, 0, 0],
                        "min_score": 50
                    },
                    {
                        "level_id":ObjectId(),
                        "index": 6,
                        "level_name": "Intermediate-3",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 50, 50, 0],
                        "min_score": 300
                    },                                                
                    {
                        "level_id":ObjectId(),
                        "index": 7,
                        "level_name": "Advanced-1",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 0, 100, 0],
                        "min_score": 350
                    },
                    {
                        "level_id":ObjectId(),
                        "index": 8,
                        "level_name": "Advanced-2",
                        "num_questions": 10,
                        "question_difficulty_distribution": [0, 0, 0, 50, 50],
                        "min_score": 400
                    },
                    {
                        "level_id":ObjectId(),
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
        
    @handle_exceptions
    def insert_metadata(self, metadata_obj):
        latest_version_document = self.get_latest_metadata()
        latest_version = latest_version_document[0]['version'] if latest_version_document.count() > 0 else 0
        metadata_obj['version'] = latest_version + 1
        res = self.collection.insert_one(metadata_obj)
        return res

    @handle_exceptions
    def get_latest_metadata(self):
        latest_document = self.collection.find({}).sort('datetime', -1).limit(1)
        return latest_document

    @handle_exceptions
    def get_level_by_level_id(self,level_id:str):
        level = self.collection.find_one(
            {"data.levels.level_id": level_id},
            {"data.levels.$": 1}
        )
        if level:
            return level['data']['levels'][0]
        else:
            return None


class Users(CollectionBase):
    def __init__(self, db) -> None:
        self.collection_name = "users"
        super().__init__(self.collection_name , db)

    @handle_exceptions
    def create_user(self,username:str,password:str,password_token:str):
        user_id = ObjectId()
        new_user = {
            "user_id": user_id,
            "username":username,
            "password":password,
            "password_token":password_token,
            "current_level_index":0,
            "levels_highscores":[],
            "settings":[]
        }
        self.collection.insert_one(new_user)
        return user_id

    @handle_exceptions
    def is_username_exists(self, username:str):
        username_filter = {
            "username": username
        }
        res = self.collection.count_documents(filter=username_filter)
        if res == 0:
            return False
        return True
    
    @handle_exceptions
    def get_user_by_id(self,user_id:str):
        self.collection.find({"user_id":ObjectId(user_id)})
        logger.info("get_user_by")
    
    @handle_exceptions
    def update_user_progress(self,user_id:str,new_data):
        # level_data = {
        #     "level_id":ObjectId(),
        #     "index": 1,
        #     "level_name": "Beginner-1",
        #     "num_questions": 5,
        #     "question_difficulty_distribution": [100, 0, 0, 0, 0],
        #     "min_score": 50
        # }
        # new_data = {
        #     "level_id":ObjectId(),
        #     "index":1,
        #     "score":100,
        # }

        existing_level = self.collection.find_one(  # = did user play this level before
            {"user_id": ObjectId(user_id), "levels_highscores.level_id": level_id},
            {"levels_highscores.$": 1}
        )
        user = self.collection.find_one({"user_id": ObjectId(user_id)}) 
        current_level_index = user.get("current_level_index", None)
        new_score = new_data['score']
        level_id = new_data['level_id']
        level_index = new_data['index']

        if existing_level: # if # user already played this level and score is lower then what it used to be leave,
            existing_highscore = existing_level['levels_highscores'][0]['highscore'] # user current highest score in this level
            if new_score < existing_highscore:
                return
        # V -- either user play new level , or user with better highscore in level he played before
        
        
        update_data = {
            "level_id":level_id,
            "index":level_index,
            "highscore":new_score,
            "date":datetime.now()
        }

        if existing_level: # user already played this level so new score is better
            self.collection.update_one(
                {"user_id": ObjectId(user_id), "levels_highscores.level_id": level_id},
                {"$set": {"levels_highscores.$": update_data}}
            )
        else: # user did not played this level before
            self.collection.update_one(
                {"user_id": ObjectId(user_id)},
                {"$push": {"levels_highscores": update_data}}
            )
        
        level = mongo.Metadata.get_level_by_level_id(level_id)
        min_score = level.get('min_score',None)
        if current_level_index < level_index and new_score > min_score: # update user current level index if the index is lower and score is higher then minimum of that level.
            self.collection.update_one(
                {"user_id": ObjectId(user_id)},
                {"$set": {"current_level_index": level_index}}
            )
    




    
    


class Questions(CollectionBase):
    def __init__(self, db) -> None:
        self.collection_name = "questions"
        super().__init__(self.collection_name , db)

    @handle_exceptions
    def create_new_question(self,
                            question:list[dict],
                            options:list[dict],
                            difficulty:int,
                            right_answer_index:int,
                            solution:str,
                            references:list[str]):
        new_question_data = {
            "question_id": ObjectId(), 
            "question": question,
            "difficulty": difficulty,
            "options": options,
            "right_answer_index": right_answer_index,
            "solution": solution,
            "references": references
        }
        self.collection.insert_one(new_question_data)

    @handle_exceptions
    def get_random_question_by_difficulty(self,difficulty:int):
        questions = list(self.collection.find({"difficulty": difficulty}))
        if questions:
            return random.choice(questions)
        else:
            return None

    @handle_exceptions
    def get_batch_random_questions(self,n, difficulty_distribution):
        if len(difficulty_distribution) != 5 or sum(difficulty_distribution) != 100:
                raise ValueError("Invalid difficulty distribution")
        questions = []
        for _ in range(n):
            random_difficulty = random.choices([1, 2, 3, 4, 5], weights=difficulty_distribution)[0]
            question = self.get_random_question_by_difficulty(random_difficulty)
            questions.append(question)  
        return questions      
    
    @handle_exceptions
    def get_level_questions(self,level_id):
        level = mongo.Metadata.get_level_by_level_id(level_id)
        num_of_question = level.get("num_questions",None)
        difficulty_distribution = level.get("difficulty_distribution",None)
        return self.get_batch_random_questions(num_of_question,difficulty_distribution)



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
