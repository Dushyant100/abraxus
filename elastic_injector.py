from elasticsearch import Elasticsearch
import requests

# trying to use the Elasetisearch library / module
client = Elasticsearch()
client.create(index = "dushyant", id = 9 ,body = {'haha':'noice','message':'added again'}, params=None, headers=None)

