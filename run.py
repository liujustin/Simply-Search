import os
import elasticsearch
import pymongo
from app import create_app
from mongo import mongo_db
from elastic import elastic_search
from config import Config
from dotenv import load_dotenv


load_dotenv()
app = create_app(os.getenv('FLASK_CONFIG'))
mongo_client = mongo_db.MongoDB(host=os.getenv("MONGO_URI"))
es = elastic_search.Elastic_Search(hosts=os.getenv("ELASTIC_HOSTS"))
mongo_db = mongo_client.initiate()
es.initiate(mongo_db)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
