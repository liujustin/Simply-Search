import elasticsearch
import json
import sys
from bson import json_util

class Elastic_Search:

    def __init__(self, hosts):
        self.hosts = hosts
        self.es = elasticsearch.Elasticsearch(self.hosts)

    def initiate(self, mongo_db):
        try:
            # mongodb cursor
            cursor = mongo_db.find({})
            # for each entry in mongodb, index an elasticsearch
            # if self.es.indices.exists(index="elasticsearch"):
            self.es.indices.delete(index="elasticsearch")
            print '---Indexing data into elastic search---'
            for document in cursor:
                print document
                self.es.index(index="elasticsearch",
                              doc_type="sample_data",
                              id=json.loads(json_util.dumps(document['_id'])).get("$oid"),
                              body={"data": document["sample_data"]["name"], "date":document["sample_data"]["date"]})
                self.es.indices.refresh(index="elasticsearch")
            # refresh indices in elastic
            print '---Data successfully indexed---'
        except:
            print "Unexpected Error: ", sys.exc_info()
    
    def search_elastic(self, query):
        """
        Searches the database for a specified query 
        """
        return self.es.search(index="elasticsearch", doc_type="sample_data", size=1000, body={ "query": {"match_phrase" : {"data": query}}})['hits']['hits']
