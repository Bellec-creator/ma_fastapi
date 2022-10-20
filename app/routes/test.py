from fastapi import APIRouter, Body, HTTPException
from app.database.connexion_mongo import get_all

router_test = APIRouter()

@router_test.get("/test")
async def hello_world():
    return {"message": "Hello World"}

@router_test.get("/test2")
async def test_string(string:str):
    return {"message": string}

@router_test.get("/test3")
async def test_mongodb():
    proprietaire = await get_all("proprietaire")
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Aucun propriétaire n'a été trouvé")
