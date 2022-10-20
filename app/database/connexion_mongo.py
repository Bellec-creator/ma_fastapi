from http.client import HTTPException
import os
import motor.motor_asyncio

MONGO_URL = os.environ.get("mongodb://192.168.35.28:27017/")
MONGO_DB = os.environ.get("fastapi")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.get_database(MONGO_DB)

async def get_all(collection: str):
    list_data = []
    data_collection = database.get_collection(collection)
    async for data in data_collection.find():
        list_data.append(data)
    return list_data