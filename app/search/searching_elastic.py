import os
import json
from elastic import Elastic_Search


def searching_elastic(search_text):
    """
    Creates an instance of elastic search and searches to see if it has results for specified search text.
    """
    es = Elastic_Search(os.getenv("ELASTIC_HOSTS"))

    result = es.search_elastic(search_text)
    display_array = []
    if result:
        for hit in result:
            display_array.append(hit)
    return display_array
