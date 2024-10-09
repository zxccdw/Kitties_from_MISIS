import asyncio
import json
import string
from random import choice
from datetime import date, datetime, timedelta
from os import getenv
from time import sleep, mktime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import List, Union, Optional
from sqlalchemy.exc import OperationalError as sqlalchemyOpError
from psycopg2 import OperationalError as psycopg2OpError

from schemas.models import *
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
        return self.session.query(User).filter_by(email=email).first() is not None
    
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email from the database"""
        user: Optional[User] = self.session.query(User).filter_by(email=email).one_or_none()
        return user
    

    # def user_exists(self, vk_id: int) -> bool:
    #     """Check if user exists in the database"""
    #     return self.session.query(User).filter_by(vk_id=vk_id).first() is not None

    # def get_users_test(self) -> dict:
    #     """Get all users from the database"""
    #     users = self.session.query(User).all()
    #     return {
    #         user.vk_id: {
    #             "wallet_public_key": user.wallet_public_key,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #         }
    #         for user in users
    #     }

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
