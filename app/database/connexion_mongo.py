from http.client import HTTPException
import os
import motor.motor_asyncio

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")
MONGO_DB = os.environ.get("MONGODB_ADDON_DB")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.get_database(MONGO_DB)

async def insert(collection:str,add_data:dict):
    data_collection = database.get_collection(collection)
    data = await data_collection.insert_one(add_data)
    new_data = await data_collection.find_one({"_id": data.inserted_id})
    return new_data
async def get_all(collection: str):
    list_data = []
    data_collection = database.get_collection(collection)
    async for data in data_collection.find():
        list_data.append(data)
    return list_data

async def drop_bd(collection:str):
    data_collection = database.get_collection(collection)
    data_collection.drop()