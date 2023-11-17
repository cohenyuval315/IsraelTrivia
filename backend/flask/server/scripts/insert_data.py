import logging
from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
import os
from db import mongo
from logger import logger
from flask_bcrypt import Bcrypt
import random
import string
import secrets

bcrypt = Bcrypt()

level_id = str(ObjectId())
level_index = 1
hard_level_id = str(ObjectId())

levels = [
    {
        "level_id": level_id,
        "level_index": level_index,
        "level_name": "Beginner-1",
        "num_statements": 5,
        "statement_difficulty_distribution": [100, 0, 0, 0, 0],
        "min_score": 50
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 2,
        "level_name": "Beginner-2",
        "num_statements": 10,
        "statement_difficulty_distribution": [50, 50, 0, 0, 0],
        "min_score": 50
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 3,
        "level_name": "Beginner-3",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 100, 0, 0, 0],
        "min_score": 50
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 4,
        "level_name": "Intermediate-1",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 50, 50, 0, 0],
        "min_score": 50
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 5,
        "level_name": "Intermediate-2",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 0, 100, 0, 0],
        "min_score": 50
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 6,
        "level_name": "Intermediate-3",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 0, 50, 50, 0],
        "min_score": 300
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 7,
        "level_name": "Advanced-1",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 0, 0, 100, 0],
        "min_score": 350
    },
    {
        "level_id": hard_level_id,
        "level_index": 8,
        "level_name": "Advanced-2",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 0, 0, 50, 50],
        "min_score": 400
    },
    {
        "level_id": str(ObjectId()),
        "level_index": 9,
        "level_name": "Advanced-3",
        "num_statements": 10,
        "statement_difficulty_distribution": [0, 0, 0, 0, 100],
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
    "date": datetime.now().isoformat(),
    "data": {
        "levels": levels,
        "statements_difficulties": [
            {"weight": 10, "time_in_sec": 10},
            {"weight": 20, "time_in_sec": 10},
            {"weight": 30, "time_in_sec": 10},
            {"weight": 40, "time_in_sec": 10},
            {"weight": 50, "time_in_sec": 10}
        ],
        "categories": [
            {"category_id": str(ObjectId()), "title": "Other"},
            {"category_id": str(ObjectId()), "title": "History"},
            {"category_id": str(ObjectId()), "title": "Politics"},
            {"category_id": str(ObjectId()), "title": "Geography"},
            {"category_id": str(ObjectId()), "title": "Sports"},
            {"category_id": str(ObjectId()), "title": "Music"},
            {"category_id": str(ObjectId()), "title": "Art"}
        ],
        "statement_types": [
            {"statement_type_id": str(ObjectId()), "title": "True Or False"},
            {"statement_type_id": str(ObjectId()), "title": "Four Options"},
            {"statement_type_id": str(ObjectId()), "title": "Two Options"}
        ],
        "supported_languages": [
            {"language_id": str(ObjectId()), "language": "English", "symbol": "en"}
        ],
        "application_settings": [
            {"setting_id": str(ObjectId()), "title": "Theme", "default_value": "white",
             "description": "application color theme"}
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


def generate_statement():
    random_int = random.randint(0, 10000000)
    diff = random.choice([1, 2, 3, 4, 5])
    random_num_links = random.choice([1, 2, 3])
    answer = random.choice([0, 1])
    refs = [generate_random_link() for i in range(random_num_links)]
    option_true_false = [
        {
            "en": "true"
        },
        {
            "en": "false"
        }
    ],

    option_answers = [
        {
            "en": f"answer {random_int}"
        },
        {
            "en": f"answer {random_int + 1}"
        }
    ]

    c = random.choice([0, 1])
    options = option_true_false if c == 1 else option_answers

    new_statement = {
        "statement_id": str(ObjectId()),
        "statement": [
            {
                "en": f"statement statement statement statement statement statement statement statement statement statement statement {random_int}"
            }
        ],
        "difficulty": diff,
        "options": options,
        "right_answer_index": answer,
        "solution": generate_random_paragraph(),
        "references": refs
    }
    return new_statement


def generate_highscore(_level_index):
    highscores = []
    for i in range(0, _level_index):
        level = levels[i]
        min_score = level['min_score']
        _level_id = level['level_id']
        score_to_pass = random.randint(min_score, min_score + 10)
        highscore = {
            "level_id": _level_id,
            "level_index": i,
            "highscore": score_to_pass,
            "date": datetime.now().isoformat()
        }
        highscores.append(highscore)

    last_level = levels[_level_index]
    last_min_score = last_level['min_score']
    last_score = random.randint(0, last_min_score)
    last_level_id = last_level['level_id']
    last_level_highscore = {
        "level_id": last_level_id,
        "level_index": _level_index,
        "highscore": last_score,
        "date": datetime.now().isoformat()
    }
    highscores.append(last_level_highscore)
    return highscores


def clean_collections():
    mongo.Metadata.drop()
    mongo.Users.drop()
    mongo.Statements.drop()



def generate_test_user():
    user_id = '0'

    #password_token = secrets.token_hex(8)  # Adjust the token length as needed

    #salted_password = password_token + "1"

    # Hash the password using Flask-Bcrypt
    # password_hash = bcrypt.generate_password_hash(salted_password).decode('utf-8')
    password_token = ""
    index = random.randint(0, 100000)
    level_index = random.randint(1, 8)
    highscores = generate_highscore(level_index)
    new_user = {
        "user_id": user_id,
        "username": "user",
        "password": "pass",
        "password_token": password_token,
        "current_level_index": level_index,
        "levels_highscores": highscores,
        "settings": []
    }
    return new_user

def generate_user():
    user_id = str(ObjectId())

    #password_token = secrets.token_hex(8)  # Adjust the token length as needed

    #salted_password = password_token + "1"

    # Hash the password using Flask-Bcrypt
    # password_hash = bcrypt.generate_password_hash(salted_password).decode('utf-8')
    password_token = ""
    index = random.randint(0, 100000)
    password_hash = f"pass{index}"
    level_index = random.randint(1, 8)
    highscores = generate_highscore(level_index)
    new_user = {
        "user_id": user_id,
        "username": f"testuser{index}",
        "password": password_hash,
        "password_token": password_token,
        "current_level_index": level_index,
        "levels_highscores": highscores,
        "settings": []
    }
    return new_user


# statements = [
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#     {
#         "statement_id": ObjectId(),
#         "statement": [
#             {
#                 "en": "statement 1"
#             }
#         ],
#         "difficulty": 1,
#         "options": [
#             {
#                 "en": "true"
#             },
#             {
#                 "en": "false"
#             }
#         ],
#         "right_answer_index": 0,
#         "solution": "this is the full description of the solution of this statement.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
#         "references": ["reflink.com", "ref2link.com"]
#     },
#
# ]


def run_script():
    clean_collections()
    num_users = 4
    num_statements = 200
    users = [generate_user() for i in range(num_users)]
    statements = [generate_statement() for i in range(num_statements)]
    user_index = 0
    statements_index = 0
    try:
        mongo.Metadata.collection.insert_one(metadata)
        
        logger.info(f"successfuly inserted metadata")
        test_user = generate_test_user()
        mongo.Users.collection.insert_one(test_user)
        for user in users:
            mongo.Users.collection.insert_one(user)

            user_index += 1
        for statement in statements:
            mongo.Statements.collection.insert_one(statement)
            statements_index += 1
    except Exception as e:
        logger.error(e)
    logger.info(f"successfuly inserted {user_index} users")
    logger.info(f"successfuly inserted {statements_index} statements")

    user_id = users[0]['user_id']
    logger.info(user_id)
    # username = users[0]['username']
    user = mongo.Users.get_user_by_id(user_id=user_id)
    # mongo.Users.update_user_progress()

    statements = mongo.Statements.get_level_statements(level_id=hard_level_id)

    new_data = {
        "level_id":level_id,
        "level_index":level_index,
        "score":9900
    }

    mongo.Users.update_user_progress(user_id=user_id,new_data=new_data)



    # is_exists_true = mongo.Users.is_username_exists(username=username)
    # is_exists_false = mongo.Users.is_username_exists(username="hello")
    # logger.info(f"user by user id: {user_id}. data: {user} ")


def test_stuff():
    pass

if __name__ == "__main__":
    # docker exec backend-backend-1 python scripts/insert_data.py
    run_script()
    test_stuff()
