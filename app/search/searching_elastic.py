import json
from elastic import Elastic_Search


def searching_elastic(search_text):
    es = Elastic_Search(hosts = [{ "host" : "localhost", "port" : 9200 }])
    result = es.search_elastic(search_text)
    display_array = []
    if result:
        for hit in result:
            display_array.append(hit)
    return display_array
