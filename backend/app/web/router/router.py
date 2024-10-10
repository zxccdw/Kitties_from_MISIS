from fastapi import APIRouter, Path, HTTPException, status, Query, Body
from typing import List, Optional, Dict

from auth.state import AuthPair
from auth.handler import signJWT
from auth.bearer import JWTBearer
from auth.models import (
    UserLoginSchema,
    UserRegistrationSchema
)
from db.manager import DBManager
from passlib.hash import bcrypt


# from schemas.product import Product
# from schemas.salepoint import SalepointReference
# from presentation.dependencies import container
# from schemas.prediction import LinkPrediciton, Relations, RelationPrediciton

router = APIRouter(prefix="")
authpair = AuthPair()
db = DBManager("logger")
db._recreate_tables()

@router.get("/ping")
async def get_server_status() -> str:
    return "pong"


@router.post("/auth/register", tags=["auth"])
async def register(user: UserRegistrationSchema = Body(...)) -> Dict[str, str]:
    if db.create_user(user):
        return {"message": "User created"}
    
    return {"message": "User already exists"}

@router.post("/auth/login", tags=["auth"])
async def login(data: UserLoginSchema = Body(...)) -> Dict[str, str]:
    user: Optional[User] = db.get_user_by_email(data.email)
    if user is None:
        return {"message": "User not found"}
    
    if not bcrypt.verify(data.password, user.hashed_password):
        return {"message": "Wrong password"}
    
    token = signJWT(user.id_user)
    # Store the token in authpair
    authpair.post(token["access_token"], user.id_user)
    return token
    
    
    
