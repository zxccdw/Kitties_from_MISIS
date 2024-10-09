import time
from typing import Dict
from os import getenv
import jwt
from shared.settings import app_settings as settings

# JWT_SECRET = getenv("JWT_SECRET")
# JWT_ALGORITHM = getenv("JWT_ALGORITHM")
# JWT_EXPIRE_TIME = int(getenv("JWT_EXPIRE_TIME")) # in seconds

JWT_SECRET = settings.jwt_secret
JWT_ALGORITHM = settings.jwt_algorithm
JWT_EXPIRE_TIME = settings.jwt_expire_time  # in seconds


def token_access_response(token: str):
    return {"access_token": token}

def token_response(access_token: str, refresh_token: str):
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


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
