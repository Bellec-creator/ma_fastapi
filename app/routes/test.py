from fastapi import APIRouter, Body, HTTPException

router_test = APIRouter()

@router_test.get("/test")
async def hello_world():
    return {"message": "Hello World"}

@router_test.get("/test2")
async def test_string(string:str):
    return {"message": string}