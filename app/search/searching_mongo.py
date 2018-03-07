import json
from mongo import MongoDB


def searching_mongo(mongo_id):
    """
    Search Mongo for a specific _id returned from elastic and returns the result.
    """
    mongodb = MongoDB(host="mongodb://localhost:27017")
    mongo_result = mongodb.search_mongo(mongo_id)
    return mongo_result
