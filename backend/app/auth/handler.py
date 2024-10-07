import time
from typing import Dict
from os import getenv
import jwt
import shared.settings as settings

# JWT_SECRET = getenv("JWT_SECRET")
# JWT_ALGORITHM = getenv("JWT_ALGORITHM")
# JWT_EXPIRE_TIME = int(getenv("JWT_EXPIRE_TIME")) # in seconds

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
JWT_EXPIRE_TIME = settings.JWT_EXPIRE_TIME  # in seconds


def token_response(token: str):
    return {"access_token": token}


def signJWT(user_id: int) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + JWT_EXPIRE_TIME}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
