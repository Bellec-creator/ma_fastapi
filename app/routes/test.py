from fastapi import APIRouter, Body, HTTPException

router_test = APIRouter()

@router_test.get("/test")
async def root():
    return {"message": "Hello World"}

@router_test.get("/test2")
async def root2(string:str):
    return {"message": string}