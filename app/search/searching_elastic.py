import json

from elastic import Elastic_Search


def searching_elastic(search_text):
    """
    Creates an instance of elastic search and searches to see if it has results for specified search text.
    """
    es = Elastic_Search(['https://jsy0vkfpyo:nu4ueefwd7@holly-2620832.us-east-1.bonsaisearch.net'])

    result = es.search_elastic(search_text)
    display_array = []
    if result:
        for hit in result:
            display_array.append(hit)
    return display_array
