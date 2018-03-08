import json
from elastic import Elastic_Search


def searching_elastic(search_text):
    es = Elasticsearch(self.hosts, http_auth=('jsy0vkfpyo','nu4ueefwd7'), verify_certs=False)
    result = es.search_elastic(search_text)
    display_array = []
    if result:
        for hit in result:
            display_array.append(hit)
    return display_array
