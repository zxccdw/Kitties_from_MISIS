from fastapi import APIRouter, Path, HTTPException, status, Query, Body, Depends
from typing import List, Optional, Dict

from auth.state import AuthPair
from auth.handler import signJWT, decodeJWT
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
# db._recreate_tables()

@router.get("/ping")
async def get_server_status() -> str:
    return "pong"


@router.post("/auth/register", tags=["auth"])
async def register(user: UserRegistrationSchema = Body(...)) -> Dict[str, str]:
    print(user.password)
    if not db.create_user(user):
        return {"message": "User already exists"}
    
    return {"message": "User created"}
    

@router.post("/auth/login", tags=["auth"])
async def login(data: UserLoginSchema = Body(...)) -> Dict[str, str]:
    user: Optional[User] = db.get_user_by_email(data.email)
    if user is None:
        return {"message": "User not found"}
    
    # print(data.password)
    # data.password = bcrypt.hash(data.password)
    # print(data.password, user.password)
    if not bcrypt.verify(data.password, user.password):
        return {"message": "Wrong password"}
    
    tokens = signJWT(user.id_user)
    db.add_tokens(user.id_user, tokens)
    authpair.post(user.id_user, tokens)
    return tokens
    

@router.post("/auth/refresh", dependencies=[Depends(JWTBearer())], tags=["auth"])
async def refresh(token: Dict[str, str] = Body(...)) -> Dict[str, str]:
    dec_token = decodeJWT(token["refresh_token"])
    if dec_token is None:
        return {"message": "Invalid token"}
    
    user_id = dec_token["user_id"]
    tokens = signJWT(user_id)
    authpair.post(user_id, tokens)
    db.add_tokens(user_id, tokens)
    return tokens
    

@router.post("/auth/logout", dependencies=[Depends(JWTBearer())], tags=["auth"])
async def logout(token: Dict[str, str] = Body(...)) -> Dict[str, str]:
    dec_token = decodeJWT(token["access_token"])
    if dec_token is None:
        return {"message": "Invalid token"}
    
    user_id = dec_token["user_id"]
    tokens = signJWT(user_id)
    authpair.post(user_id, tokens)
    db.add_tokens(user_id, tokens)
    return {"message": "Tokens deleted"}

# secure region

# end secure region

# test region
@router.get("/test/get_users", tags=["tests"])
async def get_users_test():
    return db.get_users_test()
# end test region