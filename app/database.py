import requests
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "nobel_prizes"

def fetch_and_store():
    """Fetch Nobel Prize data and store in MongoDB"""
    response = requests.get("https://api.nobelprize.org/v1/prize.json", timeout=10)
    response.raise_for_status()
    data = response.json()["prizes"]

    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["prizes"]

    # Clear existing data
    collection.delete_many({})
    collection.insert_many(data)
    print("✅ Data successfully loaded into MongoDB")

if __name__ == "__main__":
    fetch_and_store()
