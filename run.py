import os
import elasticsearch
import pymongo
from app import create_app
from mongo import mongo_db
from elastic import elastic_search
from config import Config

app = create_app(os.getenv('FLASK_CONFIG'))
mongo_client = mongo_db.MongoDB(host=Config.MONGO_URI)
es = elastic_search.Elastic_Search(hosts=Config.ELASTIC_HOST)
mongo_db = mongo_client.initiate()
es.initiate(mongo_db)

if __name__ == '__main__':
    app.run()
