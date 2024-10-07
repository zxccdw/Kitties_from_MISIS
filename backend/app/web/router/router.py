from fastapi import APIRouter, Path, HTTPException, status, Query
from typing import List, Optional

from auth.state import AuthPair

# from schemas.product import Product
# from schemas.salepoint import SalepointReference
# from presentation.dependencies import container
# from schemas.prediction import LinkPrediciton, Relations, RelationPrediciton

router = APIRouter(prefix="")
authpair = AuthPair()

@router.get("/ping")
async def get_server_status() -> str:
    return "pong"


# @router.post("/login")
# async def login() -> str: