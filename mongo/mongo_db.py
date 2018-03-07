import json
import pymongo
import sys
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self, host):
        self.host = host
        self.connection = pymongo.MongoClient(self.host)

    def initiate(self):
        try:

            # Connect to mongo on port : 27017
            print '---Connecting to MongoDB at %s---.' % self.host
            self.connection.drop_database('enerknol')
            db = self.connection.enerknol
            db_data = db.data

            print '---Opening JSON File---'
            with open('mongo/data.json') as data_file:
                data = json.load(data_file)

            holiday_list = []
            # Iterate through the "data" and assign keys to the values in it from "fields"
            print '---Parsing Data and Inserting into mongodb---'
            for holiday in data['holidays']:
                holiday_json = {}
                key = holiday["name"].replace(".", "")
                holiday_json["sample_data"] = holiday
                holiday_list.append(holiday_json.copy())
                db_data.replace_one({"sample_data": {"name": key}}, holiday_json, upsert=True)
            print '---Data Inserted SuccessFully---'

            return db_data

        except:
            print "Unexpected Error: ", sys.exc_info()
    
    def search_mongo(self, id):
        """
        Searches the database for a specified query 
        """
        return self.connection.enerknol.data.find_one({"_id": ObjectId(id)})
        
    
