from fastapi import APIRouter, Path, HTTPException, status, Query
from typing import List, Optional, Dict

from auth.state import AuthPair
from auth.handler import signJWT
from auth.bearer import JWTBearer
from auth.models import (
    UserLoginSchema
)

from db.manager import DBManager


# from schemas.product import Product
# from schemas.salepoint import SalepointReference
# from presentation.dependencies import container
# from schemas.prediction import LinkPrediciton, Relations, RelationPrediciton

router = APIRouter(prefix="")
authpair = AuthPair()
# db = DBManager("logger")

@router.get("/ping")
async def get_server_status() -> str:
    return "pong"


@api.post("/auth/login", tags=["auth"])
async def login(data: UserLoginSchema = Body(...)) -> Dict[str, str]:
    user: Optional[User] = db.auth(data.email, data.password)
    
    if user is None:
        return {"message": "User not found"}

        
    token = signJWT(user_id)
    authpair.post(token["access_token"], user_id)
    return token
    

# @router.post("/login")
# async def login() -> str: