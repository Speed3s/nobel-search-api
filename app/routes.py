from fastapi import FastAPI, Query
from pymongo import MongoClient
from fuzzywuzzy import process
from bson import ObjectId


app = FastAPI()

MONGO_URI = "mongodb://mongodb:27017"
DB_NAME = "nobel_prizes"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["prizes"]

def convert_objectid(doc):
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

@app.get("/search/")
def search_nobel_prizes(
    name: str = Query(None, description="Search by laureate's name"),
    category: str = Query(None, description="Search by prize category"),
    motivation: str = Query(None, description="Search by motivation")
):
    query = {}

    if name:
        laureates = collection.find({}, {"laureates": 1})
        all_names = [
            laureate["firstname"] + " " + laureate.get("surname", "")
            for doc in laureates if "laureates" in doc
            for laureate in doc.get("laureates", [])
        ]
        best_match, score = process.extractOne(name, all_names)
        if score > 60:
            query["laureates.firstname"] = {"$regex": best_match, "$options": "i"}

    if category:
        query["category"] = {"$regex": category, "$options": "i"}

    if motivation:
        query["laureates.motivation"] = {"$regex": motivation, "$options": "i"}

    results = list(collection.find(query))


    results = [convert_objectid(doc) for doc in results]    
    return {"results": results}

