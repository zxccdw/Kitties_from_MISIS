from pydantic import BaseModel, Field
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from enum import Enum
from datetime import datetime


class UserRegistrationSchema(BaseModel):
    first_name: str = Field(...)
    second_name: str = Field(...)
    third_name: Optional[str] = Field(None)
    email: str = Field(...)
    date_of_birth: Optional[str] = Field(None)
    sex: str = Field(None)
    fan_status: Optional[str] = Field(None)
    avatar_url: Optional[str] = Field(None)
    password: str = Field(..., min_length=8, max_length=64)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "Ivan",
                "second_name": "Ivanov",
                "email": "example@example.com",
                "sex": "male",
                "fan_status": "default",
                "avatar_url": "https://example.com/avatar.jpg",
                "password": "example"
            }
        }
        
        
class UserLoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(..., min_length=8, max_length=64)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@example.com",
                "password": "example"
            }
        }


class UserSessionSchema(BaseModel):
    id_session: int = Field(...)
    id_user: int = Field(...)
    refresh_token: str = Field(...)
    expires_at: datetime = Field(...)
    created_at: datetime = Field(...)
    last_used_at: datetime = Field(...)
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_session": 1,
                "id_user": 1,
                "refresh_token": "token",
                "expires_at": "2024-20-07 13:00:00.956741",
                "created_at": "2024-10-07 13:00:00.956741",
                "last_used_at": "2024-10-07 13:00:00.956741"
            }
        }
        