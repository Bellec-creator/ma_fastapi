from http.client import HTTPException
import os
import motor.motor_asyncio

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")
MONGO_DB = os.environ.get("MONGODB_ADDON_DB")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.get_database(MONGO_DB)

async def get_all(collection: str):
    list_data = []
    data_collection = database.get_collection(collection)
    async for data in data_collection.find():
        list_data.append(data)
    return list_data