import json
import pymongo
import sys
import elasticsearch
from bson.objectid import ObjectId
from bson import json_util

es = elasticsearch.Elasticsearch(hosts = [{ "host" : "localhost", "port" : 9200 }])

try:
    print '---Opening JSON File---'
    with open('data.json') as data_file:
        data = json.load(data_file)

    holiday_list = []
    # Iterate through the "data" and assign keys to the values in it from "fields"
    print '---Parsing Data for inserting into mongodb---'
    for holiday in data['holidays']:
        holiday_json = {}
        key = holiday["name"].replace(".", "")
        holiday_json["holiday"] = holiday
        holiday_list.append(holiday_json.copy())

	# Connect to mongo on port : 27017
    print '---Connecting to MongoDB at 27017---.'
    connection = pymongo.MongoClient(host="mongodb://localhost:27017")
    db = connection.elasticdata
    data = db.data
	
    print '---Inserting Data in MongoDB---'
    data.insert(holiday_list)
    print '---Data Inserted SuccessFully---'

    # mongodb cursor
    cursor = data.find({})
    # for each entry in mongodb, index an elasticsearch
    print '---Indexing data into elastic search---'
    for document in cursor:
        es.index(index="elasticdata",
                 doc_type="holiday",
                 id=json.loads(json_util.dumps(document['_id'])).get("$oid"),
                 body={"data": document["holiday"]["name"]})
    print '---Data successfully indexed---'
    x = es.get(index="elasticdata", doc_type="holiday", id="5a9f5569eac0b9c9dd46bf48")
    #this print statement gets the object id!!!!!!
    print data.find_one({'_id': ObjectId("5a9f5569eac0b9c9dd46bf48") })

except:
    print "Unexpected Error: ", sys.exc_info()
