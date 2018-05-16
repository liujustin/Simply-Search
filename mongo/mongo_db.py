import json
import pymongo
import sys
from bson.objectid import ObjectId

class MongoDB:
    def __init__(self, host):
        self.host = host
        self.connection = pymongo.MongoClient(self.host)

    def initiate(self):
        """
        Initializes mongodb and returns a database instance with the data read in from data.json
        """

        try:
            # Connecting to mongo
            print '---Connecting to MongoDB at %s---.' % self.host

            # dropping current database if it exists so we can start fresh
            self.connection.drop_database('searchme')
            db = self.connection.searchme
            db_with_data = db.data

            # Open json file that contains all the calendar events
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
                db_with_data.replace_one({"sample_data": {"name": key}}, holiday_json, upsert=True)
            print '---Data Inserted SuccessFully---'

            return db_with_data
        except:
            print "Unexpected Error: ", sys.exc_info()
    
    def search_mongo(self, id):
        """
        Searches the database for a specified query 
        """
        
        return self.connection.searchme.data.find_one({"_id": ObjectId(id)})
        
    
