from datetime import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from pydantic.networks import EmailStr
from app.models.utils import PyObjectId

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    status: str
    surname: str
    name: str
    mail: EmailStr
    password: str
    vpn: str
    member_of: List
    departement: List
    projects: List
    role: str
    current_project: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "status": "present",
                "surname": "Corentin",
                "name": "Bellec",
                "mail": "belleccorentin44@gmail.com",
                "password": "1234",
                "vpn": "vpn",
                "member_of": ["TS7", "Droners", "Gus"],
                "departement": ["prod"],
                "projects":["Totally spies", "gus", "droners"],
                "role": "dev",
                "current_project": "Totally spies"
            }
        }


