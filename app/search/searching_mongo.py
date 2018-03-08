import os
import json
from mongo import MongoDB


def searching_mongo(mongo_id):
    """
    Search Mongo for a specific _id returned from elastic and returns the result.
    """
    mongodb = MongoDB(host=os.getenv("MONGO_URI"))
    mongo_result = mongodb.search_mongo(mongo_id)
    return mongo_result
