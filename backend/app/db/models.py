from sqlalchemy import (
    Column,
    Text,
    BigInteger,
    MetaData,
    DateTime,
    Numeric,
    String,
    JSON,
    Enum,
    ForeignKey,
    Boolean
)
from sqlalchemy.orm import declarative_base, relationship
import enum


Base = declarative_base()
# Base.metadata = MetaData(schema="Kokoc")

class FanRole(enum.Enum):
    default = "default"
    fan = "fan"
    super_fan = "super_fan"
    

class Gender(enum.Enum):
    male = "male"
    female = "female"
    
    
class User(Base):
    __tablename__ = "user"

    id_user = Column(BigInteger, primary_key=True)
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    third_name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(String(10), nullable=True)
    sex = Column(String(10), nullable=True)
    fan_status = Column(Enum(FanRole), default=FanRole.default)
    avatar_url = Column(String(255), nullable=True)
    is_staff = Column(Boolean, default=False)
    hashed_password = Column(String(255), nullable=False)
    
    event_user_rel = relationship("GameEventUser")
    comment_rel = relationship("Comment")
    publication_rel = relationship("Publication")
    user_session_rel = relationship("UserSession")


class UserSession(Base):
    __tablename__ = "user_session"
    
    id_session = Column(BigInteger, primary_key=True)
    id_user = Column(BigInteger, ForeignKey("user.id_user"), nullable=False)
    refresh_token = Column(String(255), nullable=False)
    expires_at = Column(DateTime(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    last_used_at = Column(DateTime(), nullable=False)
    

class GameEvent(Base):
    __tablename__ = "event"
    
    id_event = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=True)
    people_limit = Column(BigInteger, nullable=True)
    location = Column(String(255), nullable=True)
    stream_url = Column(String(255), nullable=True)
    
    event_user_rel = relationship("GameEventUser")
    

class GameEventUser(Base):
    __tablename__ = "event_user"
    
    id_user = Column(BigInteger, ForeignKey("user.id_user"), primary_key=True)
    id_event = Column(BigInteger, ForeignKey("event.id_event"), primary_key=True)
    register_date = Column(DateTime(), nullable=False)
    
    
class Publication(Base):
    __tablename__ = "publication"
    
    id_publication = Column(BigInteger, primary_key=True)
    id_user = Column(BigInteger, ForeignKey("user.id_user"), nullable=False)
    title = Column(String(255), nullable=False)
    short_description = Column(String(255), nullable=False)
    publication_date = Column(DateTime(), nullable=False)
    text = Column(Text, nullable=False)
    
    
class PublicationLinkedS3(Base):
    __tablename__ = "publication_linked_s3"
    
    id_file = Column(BigInteger, primary_key=True)
    id_publication = Column(BigInteger, ForeignKey("publication.id_publication"), nullable=False)
    url = Column(String(255), nullable=False)
    date = Column(DateTime(), nullable=False)
    priority = Column(BigInteger, nullable=False)
    
    
class Comment(Base):
    __tablename__ = "comment"
    
    id_comment = Column(BigInteger, primary_key=True)
    id_user = Column(BigInteger, ForeignKey("user.id_user"), nullable=False)
    id_publication = Column(BigInteger, ForeignKey("publication.id_publication"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(DateTime(), nullable=False)
    

class FootballPlayer(Base):
    __tablename__ = "football_player"
    
    id_player = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)
    third_name = Column(String(255), nullable=True)
    info = Column(JSON, nullable=False) # JSON type in kraft!!!
