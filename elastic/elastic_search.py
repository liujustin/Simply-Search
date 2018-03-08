import os
import elasticsearch
import json
import sys
from bson import json_util

class Elastic_Search:

    def __init__(self, hosts):
        self.hosts = hosts
        print "hosts", hosts
        self.es = elasticsearch.Elasticsearch(hosts=hosts, http_auth=('jsy0vkfpyo','nu4ueefwd7'), verify_certs=False)

    def initiate(self, mongo_db):
        """
        Takes in a mongo_db instance, initializes elastic search and indexes the results from mongo.
        """
        try:
            # mongodb cursor
            cursor = mongo_db.find({})
            # for each entry in mongodb, index an elasticsearch
            if self.es.indices.exists(index="elasticsearch"):
                self.es.indices.delete(index="elasticsearch")
            self.es.indices.create(index='elasticsearch', ignore=400)
            print '---Indexing data into elastic search---'
            for document in cursor:
                self.es.index(index="elasticsearch",
                              doc_type="sample_data",
                              id=json.loads(json_util.dumps(document['_id'])).get("$oid"),
                              body={"data": document["sample_data"]["name"], "date":document["sample_data"]["date"]})
                self.es.indices.refresh(index="elasticsearch")
            # refresh indices in elastic
            print '---Data successfully indexed---'
        except:
            print "Unexpected Error: ", sys.exc_info()
    
    def search_elastic(self, search_term):
        """
        Searches the database for a specified search term and returns the result.
        """
        return self.es.search(index="elasticsearch", doc_type="sample_data", size=1000, body={"query":{"match_phrase":{"data": search_term}}})['hits']['hits']
