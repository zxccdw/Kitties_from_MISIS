from fastapi import APIRouter, Path, HTTPException, status, Query, Body
from typing import List, Optional, Dict
import wikipedia

# from schemas.product import Product
# from schemas.salepoint import SalepointReference
# from presentation.dependencies import container
# from schemas.prediction import LinkPrediciton, Relations, RelationPrediciton

router = APIRouter(prefix="")

def get_url_by_word(word: str, max_depth: int = 5) -> Dict[str, str]:
    urls = {}
    try:
        result = wikipedia.search(word, results=max_depth * 2)
    
        for obj in result[:max_depth]:
            page_title = obj.replace(' ', '_')
            url = f"https://ru.wikipedia.org/wiki/{page_title}"
            urls[obj.title()] = url
        
    except wikipedia.exceptions.WikipediaException as e:
        raise HTTPException(status_code=400, detail=f"Wikipedia API error: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    # print(urls)
    return urls
    
    
@router.get("/ping")
def get_server_status() -> str:
    return "pong"


@router.get("/wikipedia/{word}")
def get_urls_from_wikipedia(word: str, max_depth: Optional[int] = 5) -> Dict[str, str]:
    res = get_url_by_word(word, max_depth)
    return res
