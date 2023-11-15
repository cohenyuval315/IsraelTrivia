from bson import ObjectId
from json import JSONEncoder

#JSON Encoder
class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:            
            return JSONEncoder.default(obj, **kwargs)


def generate_id():
    new_object_id = ObjectId()
    return new_object_id
