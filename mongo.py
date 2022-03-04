import os
import glob
import json
from pymongo import MongoClient

myClient = MongoClient("mongodb://localhost:27017/")

db = myClient["hw2"]
collection = db["factbook"]
path = "./factbook.json/"
dirs = os.listdir(path)
collection.drop()

for folder in glob.glob(path + "*"):
    if not os.path.isdir(folder):
        continue
    for file in glob.glob(folder + "/*.json"):
        with open(file, 'r') as f:
            data = json.load(f)
            collection.insert_one(data)
            print('Added: ' + file)