import asyncio
import json
import string
from datetime import datetime
from os import getenv
from time import sleep, mktime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc
from typing import List, Union, Optional, Dict
from sqlalchemy.exc import OperationalError as sqlalchemyOpError
from psycopg2 import OperationalError as psycopg2OpError
from passlib.hash import bcrypt
from shared.settings import app_settings

from schemas.models import (
    UserSchema,
    GameEventSchema
)

from db.models import *

class DBManager:
    def __init__(self, log):
        # self.pg_user = getenv("PG_USER")
        # self.pg_pass = getenv("PG_PASS")
        # self.pg_host = getenv("PG_HOST")
        # self.pg_port = getenv("PG_PORT")
        # self.pg_db = getenv("PG_DB")
        self.pg_user = "postgres"
        self.pg_pass = "00000000"
        self.pg_host = "localhost"
        self.pg_port = 5432
        self.pg_db = "Misis_Kitties"
        
        self.log = log
        # self.itools = itools
        connected = False
        while not connected:
            try:
                self._connect()
            except (sqlalchemyOpError, psycopg2OpError):
                sleep(2)
            else:
                connected = True
        self._update_db()

    def __del__(self):
        """Close the database connection when the object is destroyed"""
        self._close()

    # region Connection setup
    def _connect(self) -> None:
        """Connect to the postgresql database"""
        self.engine = create_engine(
            f"postgresql+psycopg2://{self.pg_user}:{self.pg_pass}@{self.pg_host}:{self.pg_port}/{self.pg_db}",
            pool_pre_ping=True,
        )
        Base.metadata.bind = self.engine
        db_session = sessionmaker(bind=self.engine)
        self.session = db_session()

    def _close(self) -> None:
        """Closes the database connection"""
        self.session.close_all()

    def _recreate_tables(self) -> None:
        """Recreate tables in DB"""
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def _update_db(self) -> None:
        """Create the database structure if it doesn't exist (update)"""
        # Create the tables if they don't exist
        Base.metadata.create_all(self.engine)

    # endregion ------------
    
    def user_exists(self, email: int) -> bool:
        """Get user by email from the database"""
        return self.session.query(User).filter_by(email=email).first() is not None
    
    def tokens_exists(self, user_id: int) -> bool:
        """Get tokens by user_id from the database"""
        return self.session.query(UserSession).filter_by(id_user=user_id).first() is not None
    
    def create_user(self, user: UserSchema) -> bool:
        if self.user_exists(user.email):
            return False
        new_user = User(**user.dict())
        new_user.password = bcrypt.hash(user.password)
        self.session.add(new_user)
        self.session.commit()
        return True
    
    def get_user_by_email(self, email: str) -> Optional[UserSchema]:
        return self.session.query(User).filter_by(email=email).one_or_none()
    
    def is_admin(self, user_id: int) -> bool:
        return self.session.query(User).filter_by(id_user=user_id, is_staff=True).first() is not None
    
    def add_admin(self, user_id: int) -> None:
        if self.user_exists(user_id):
            self.session.query(User).filter_by(id_user=user_id).update(
                {User.is_admin: True}
            )
            self.session.commit()
            
    def add_admin_test(self):
        admin_user = User(
            email="admin@example.com",
            password=bcrypt.hash("adminadmin"),
            first_name="admin",
            second_name="admin",
            sex="male",
            date_of_birth="01-01-1990",
            is_staff=True
        )
        self.session.add(admin_user)
        self.session.commit()
    
    def add_tokens(self, id_user: int, tokens: Dict[str, str]) -> None:
        """Add or update tokens in the database"""
        if self.tokens_exists(id_user):
            self.session.query(UserSession).filter_by(id_user=id_user).update(
                {
                    UserSession.refresh_token: tokens["refresh_token"],
                    UserSession.access_token: tokens["access_token"],
                    UserSession.created_at: datetime.now(),
                    UserSession.last_used_at: datetime.now(),
                }
            )
        else:
            new_tokens = UserSession(
                id_user=id_user,
                refresh_token=tokens["refresh_token"],
                access_token=tokens["access_token"],
                created_at=datetime.now(),
                last_used_at=datetime.now(),
            )
            self.session.add(new_tokens)
        self.session.commit()
    
    def get_tokens(self, id_user: int) -> Optional[Dict[str, str]]:
        """Get tokens by user_id from the database"""
        tokens = self.session.query(UserSession).filter_by(id_user=id_user).first()
        if tokens is None:
            return None
        
        return {
            "access_token": tokens.access_token,
            "refresh_token": tokens.refresh_token
        }

    def event_exists(self, id_event: int) -> bool:
        return self.session.query(GameEvent).filter_by(id_event=id_event).first() is not None
    
    def get_users_test(self) -> Dict[int, dict]: # test function
        """Get all users from the database"""
        users = self.session.query(User).all()
        return {
            user.id_user: {
                "email": user.email,
                "password": user.password,
                "fist_name": user.first_name,
                "second_name": user.second_name,
                "sex": user.sex,
                "date_of_birth": user.date_of_birth   
            }
            for user in users
        }

    def get_events(self, max_events: int) -> Dict[int, dict]: # hz
        events = self.session.query(GameEvent).order_by(desc(GameEvent.start_date)).limit(max_events).all()
        ar: List[GameEventSchema] = []
        return {
            event.id_event: {
                "description": event.description,
                "title": event.title,
                "start_date": event.start_date,
                "end_date": event.end_date,
                "people_limit": event.people_limit,
                "location": event.location,
                "stream_url": event.stream_url
            }
            for event in events
        }
        
    def get_event(self, id_event: int) -> Dict[int, dict]:
        if self.event_exists(id_event):
            event = self.session.query(GameEvent).filter_by(id_event=id_event).one()
            return {
                event.id_event: {
                    "description": event.description,
                    "title": event.title,
                    "start_date": event.start_date,
                    "end_date": event.end_date,
                    "people_limit": event.people_limit,
                    "location": event.location,
                    "stream_url": event.stream_url
                }
            }
        
    def add_event(self, event: GameEventSchema) -> None:
        game_event = GameEvent(**event.dict())
        self.session.add(game_event)
        self.session.commit()  
        
    def update_event(self, event: GameEventSchema) -> None:
        if self.event_exists(event.id_event):
            self.session.query(GameEvent).filter_by(id_event=event.id_event).update(
                {
                    GameEvent.title: event.title,
                    GameEvent.description: event.description,
                    GameEvent.start_date: event.start_date,
                    GameEvent.end_date: event.end_date,
                    GameEvent.people_limit: event.people_limit,
                    GameEvent.location: event.location,
                    GameEvent.stream_url: event.stream_url
                }
            )
            self.session.commit()
            
    def sign_user_to_event(self, user_id: int, event_id: int) -> bool:
        event_info = self.get_event(event_id)
        if event_info is None:
            return False
        
        if event_info["end_date"] < datetime.now():
            return False
        
        signed_user = GameEventSchema(
            id_user=user_id,
            id_event=event_id,
            created_at=datetime.now(),
        )
        self.session.add(signed_user)
        self.session.commit()
        return True
        
    # def get_users(self) -> dict:
    #     """Get all users from the database"""
    #     users = self.session.query(User).all()
    #     return {
    #         user.vk_id: {
    #             "wallet_public_key": user.wallet_public_key,
    #         }
    #         for user in users
    #     }

    # def auth(
    #     self, vk_id: int, wallet_public_key: str, first_name: str, last_name: str
    # ) -> bool:
    #     """Create a new user in the database
    #     Returns True if successful, False if user is not found and no wallet is provided"""
    #     user_exists = self.user_exists(vk_id)
    #     if not wallet_public_key and not user_exists:
    #         return False
    #     if not first_name and not user_exists:
    #         return False
    #     if not last_name and not user_exists:
    #         return False
    #     if user_exists:
    #         if wallet_public_key:
    #             self.update_user_wallet(vk_id, wallet_public_key)
    #         return True
    #     new_user = User(
    #         vk_id=vk_id,
    #         first_name=first_name,
    #         last_name=last_name,
    #         wallet_public_key=wallet_public_key,
    #     )
    #     self.session.add(new_user)
    #     self.session.commit()
    #     return True

    # def get_user_object(self, vk_id: int, wallet: str = "", fname: str = "", lname: str = "") -> User:
    #     """Get user object from the database"""
    #     user = self.session.query(User).filter(User.id == vk_id).one_or_none()
    #     if user is None:
    #         # Create user
    #         self.auth(vk_id, wallet, fname, lname)

    # def update_user_wallet(self, vk_id: int, wallet_public_key: str) -> None:
    #     """Update user wallet if it's different from the one in the database"""
    #     user = self.get_user_object(vk_id)
    #     # if user.wallet_public_key != wallet_public_key:
    #     #     user.wallet_public_key = wallet_public_key
    #     self.session.commit()

    # def get_user_wallet(self, vk_id: int):
    #     """Get user wallet from the database"""
    #     user = self.session.query(User).filter(User.id == vk_id).one_or_none()
    #     return user.wallet_public_key
    # def get_user(vk_id: int) -> User:
    #     return self.session.query(User).filter(User.id == vk_id).one_or_none()

    # def get_user_first_name(self, vk_id: int) -> str:
    #     """Get user first name from the database"""
    #     return (
    #         self.session.query(User).filter(User.id == vk_id).one_or_none().first_name
    #     )

    # def get_user_last_name(self, vk_id: int) -> str:
    #     """Get user last name from the database"""
    #     return self.session.query(User).filter(User.id == vk_id).one_or_none().last_name

    # def get_user_id(self, vk_id: int) -> User | None:
    #     return self.session.query(User).filter(User.id == vk_id).one_or_none()

    # def create_event(
    #     self,
    #     event_data: EventCreateSchema,
    #     user_id: int,
    #     collection_id: str,
    # ):
    #     db_event = Event(
    #         title=event_data.title,
    #         description=event_data.description,
    #         place=event_data.place,
    #         ownerID=self.get_user_id(user_id),
    #         datetime=event_data.datetime,
    #         collectionID=collection_id,
    #     )
    #     self.session.add(db_event)
    #     self.session.commit()
    #     return db_event
