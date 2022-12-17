import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost:27017/") 
print(mongoClient)
db = mongoClient['TIMES']
collection =db['project']
dictionary = {'heading':'head','LINK':'Link','DATE':4}
dictionary = {'heading':'head','LINK':'Link','DATE':5}
collection.insert_one(dictionary)