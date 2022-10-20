from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.database.connexion_mongo import get_all, insert
from app.models.user import User

router_test = APIRouter()

@router_test.get("/test")
async def hello_world():
    return {"message": "Hello World"}

@router_test.get("/test2")
async def test_string(string:str):
    return {"message": string}

@router_test.get("/all_users")
async def test_mongodb():
    proprietaire = await get_all("user")
    if proprietaire:
        return proprietaire
    raise HTTPException(404, "Aucun user n'a été trouvé")

async def post_proprietaire(proprietaire_data : User = Body(...)):
    user = jsonable_encoder(proprietaire_data)
    new_proprietaire = await insert("user", user)
    if new_proprietaire:
        return new_proprietaire
    raise HTTPException(500, "Erreur technique lors de l'opération")
