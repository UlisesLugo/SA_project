from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    ARRAY
)
from database_session import DatabaseSession
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(
    metadata=MetaData(),
)

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)

    def to_dict(self):
        return {"movie_title":self.movie_title, "preference_key":self.preference_key, "rating":self.rating}

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    email = Column(String, unique=True)
    preferences = Column(ARRAY(Integer))
    token = Column(String, unique=True)

    def to_dict(self):
        return {"username":self.username, 
                "email":self.email, 
                "preferences":self.preferences, 
                "token":self.token
                }

class Models():
    def start_mappers():
        session = DatabaseSession()
        Base.metadata.create_all(session.engine)
