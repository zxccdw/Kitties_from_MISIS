from fastapi import APIRouter, Path, HTTPException, status, Query, Body
from typing import List, Optional, Dict
import requests

# from schemas.product import Product
# from schemas.salepoint import SalepointReference
# from presentation.dependencies import container
# from schemas.prediction import LinkPrediciton, Relations, RelationPrediciton

router = APIRouter(prefix="")

def get_phrase_from_request():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&key=random&format=jsonp&lang=ru&jsonp=?"
    json = requests.get(url)
    # print(json.json)
    return json.text    
    
    
@router.get("/ping")
def get_server_status() -> str:
    return "pong"


@router.get("/quotations/")
def get_quotations():
    res = get_phrase_from_request()
    return res
