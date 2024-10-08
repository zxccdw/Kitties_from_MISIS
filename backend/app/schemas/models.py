from pydantic import BaseModel, Field
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from enum import Enum
from datetime import datetime

class UserSchema(BaseModel):
    id_user: int = Field(...)
    first_name: str = Field(...)
    second_name: str = Field(...)
    third_name: Optional[str] = Field(None)
    email: str = Field(...)
    date_of_birth: Optional[str] = Field(None)
    sex: str = Field(None)
    fan_status: Optional[str] = Field(None)
    avatar_url: Optional[str] = Field(None)
    is_staff: bool = Field(False)

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "id_user": 1,
                "first_name": "Ivan",
                "second_name": "Ivanov",
                "email": "example@example.com",
                "sex": "male",
                "fan_status": "default",
                "is_staff": False
            }
        }


class GameEventSchema(BaseModel):
    id_event: int = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    start_date: datetime = Field(...) # unix time
    end_date: Optional[datetime] = Field(None) # unix time
    people_limit: Optional[int] = Field(None)
    location: Optional[str] = Field(None)
    stream_url: Optional[str] = Field(None)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_event": 1,
                "title": "Game event title",
                "description": "Game event description",
                "start_date": "2024-10-07 13:00:00.956741",
                "end_date": "2024-10-07 16:00:00.956741",
                "people_limit": 10,
                "location": "Moscow, Russia",
                "stream_url": "http/stream.com"
            }
        }
        

class PublicationSchema(BaseModel):
    id_publication: int = Field(...)
    id_user: int = Field(...)
    title: str = Field(...)
    short_description: str = Field(...)
    publication_date: datetime = Field(...) # unix time
    text : str = Field(...)
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_publication": 1,
                "id_user": 1,
                "title": "Publication title",
                "short_description": "Publication short description",
                "publication_date": "2024-10-07 13:00:00.956741",
                "text": "Publication text"
            }
        }
        
        
class CommentSchema(BaseModel):
    id_comment: int = Field(...)
    id_user: int = Field(...)
    id_publication: int = Field(...)
    text: str = Field(...)
    date: datetime = Field(...) # unix time
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id_comment": 1,
                "id_user": 1,
                "id_publication": 1,
                "text": "Comment text",
                "date": "2024-10-07 13:00:00.956741"
            }
        }
