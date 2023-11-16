from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
import os
from db import mongo
from logger import logger
import random
import string

levels =  [
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
]


levels_ids = [level['level_id'] for level in levels]

def get_level(level_id):
    for l in levels:
        if l['level_id'] == level_id:
            return l
    logger.info("Not Found Level")

metadata = {
            "version": 0,
            "date": datetime.now(),                
            "data": {
                "levels": levels,
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
      

levels_ids = metadata 

def generate_random_link(length=10):
    characters = string.ascii_letters + string.digits
    random_link = ''.join(random.choice(characters) for _ in range(length))
    return f"https://example.com/{random_link}"


def generate_random_paragraph(sentence_count=5, words_per_sentence=10):
    word_list = [
        "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
        "adipiscing", "elit", "sed", "do", "eiusmod", "tempor",
        "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"
    ]

    paragraphs = []

    for _ in range(sentence_count):
        sentence = " ".join(random.sample(word_list, words_per_sentence))
        paragraphs.append(sentence.capitalize() + ".")

    return " ".join(paragraphs)


def generate_question():
    random_int = random.randint(0,10000000)
    diff = random.choice([1,2,3,4,5])
    random_num_links = random.choice([1,2,3])
    answer = random.choice([0,1])
    refs = [generate_random_link() for i in range(random_num_links)]
    option_true_false = [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
    ],

    option_answers = [
        {
            "en":f"answer {random_int}"
        },
        {
            "en":f"answer {random_int + 1}"
        }
    ]

    c = random.choice([0,1])
    options = option_true_false if c == 1 else option_answers 

    new_question = {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": f"question question question question question question question question question question question {random_int}"
            }
        ],
        "difficulty": diff,
        "options": options,
        "right_answer_index": answer,
        "solution": generate_random_paragraph(),
        "references": refs
    }
    return new_question


def generate_highscore(level_index):
    highscores = [] 
    for i in range(1,level_index - 1):
        
        level = levels[level_index]    
        min_score = level['min_score']
        level_id = level['level_id']
        score_to_pass = random.randint(min_score,min_score + 10)
        highscore = {
            "level_id": level_id,
            "level_index": level_index,
            "highscore": score_to_pass,
            "date": datetime.now()             
        }
        highscores.append(highscore)
    
    last_level = levels[level_index]
    last_min_score= last_level['min_score'] 
    last_score = random.randint(0,last_min_score)
    last_level_id = last_level['level_id']
    last_level_highscore = {
            "level_id":last_level_id,
           "level_index": level_index,
            "highscore": last_score,
            "date": datetime.now()                  
    }
    highscores.append(last_level_highscore)
    return highscores
    



def clean_collections():
    mongo.Metadata.drop()
    mongo.Users.drop()
    mongo.Questions.drop()

def generate_user():
    user_id = ObjectId()
    index = random.randint(0,100000)
    level_index = random.randint(1,8)
    highscores = generate_highscore(level_index)
    new_user = {
        "user_id": user_id,
        "username":f"testuser{index}",
        "password":"",
        "password_token":"",
        "current_level_index":level_index,
        "levels_highscores":highscores,
        "settings":[]
    }
    return new_user

questions = [
    {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },

        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },

        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },

        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
        {
        "question_id": ObjectId(), 
        "question": [
            {
                "en": "question 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    },
    
]

def run_script():
    clean_collections()
    num_users = 4
    num_questions = 200
    users = [generate_user() for i in range(num_users)]
    questions = [generate_question() for i in range(num_questions)]
    user_index  = 0
    questions_index = 0
    try:
        mongo.Metadata.collection.insert_one(metadata)
        for user in users:
            mongo.Users.collection.insert_one(user)
            user_index +=1 
        for question in questions:
            mongo.Questions.collection.insert_one(question)
            questions_index +=1 
    except Exception as e:
        logger.error(e)
    logger.info(f"successfuly inserted {num_users} users") 
    logger.info(f"successfuly inserted {num_questions} questions")

if __name__ == "__main__":
    # docker exec backend-backend-1 python scripts/insert_data.py
    run_script()
