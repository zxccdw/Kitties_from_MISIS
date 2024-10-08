from pydantic import BaseModel, Field
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from enum import Enum
from datetime import datetime


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
