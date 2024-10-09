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
    db.create_user(user)
    
    



@router.post("/auth/login", tags=["auth"])
async def login(data: UserLoginSchema = Body(...)) -> Dict[str, str]:
    user: Optional[User] = db.get_user_by_email(data.email)
    
    if user is None:
        return {"message": "User not found"}

    if 
        
    token = signJWT(user_id)
    authpair.post(token["access_token"], user_id)
    return token
    
