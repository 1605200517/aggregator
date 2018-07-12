import pymongo
import sys, datetime, urllib, json, requests
import jsonpath
from pymongo import MongoClient


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

#mongodb://alice:abc123@localhost:27017
print ("a")
print (sys.argv[1])
print("b")
client = MongoClient(sys.argv[1])

sonarqube_url="https://sonarcloud.io/api/measures/component?componentId=AWSJ6-l9XvYvXQrbHVtp&metricKeys=security_rating"
r = requests.get(sonarqube_url)
obj_json= r.json()
print (obj_json)
pp_json(obj_json)

result=jsonpath.jsonpath(obj_json, "$..measures..value")
print(result)



exit(0)

db = client.fiwareqa
collection = db.test_collection

measurement = {"organization": "fiware",
         "product": "authzforce",
         "repo":"https://github.com/authzforce/server.git",
         "change_id":"abcdef123",
         "measurement":"static_analysis",
         "label":"A",
         "rating:":"0.7",
         "date": datetime.datetime.utcnow()}
         
         
collection.insert_one(measurement).inserted_id
         
