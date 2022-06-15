import csv
import os
from datetime import datetime
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
)
from movies.database_session import DatabaseSession
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
    preference_key = Column(Integer)
    token = Column(String, unique=True)

def start_mappers():
    session = DatabaseSession()
    Base.metadata.create_all(session.engine)

    if session.query(Movie).first() is None:
        base_dir = os.path.dirname(os.path.realpath(__file__))
        with open(f"{base_dir}/movie_results.csv", "r") as movies_csv:
            csv_reader = csv.DictReader(movies_csv, skipinitialspace=True)
            for i, row in enumerate(csv_reader):
                session.add(Movie(
                    movie_id=i,
                    preference_key=int(row["preference_key"]),
                    movie_title=row["movie_title"],
                    rating=float(row["rating"]),
                    year=int(row["year"]),
                    create_time=datetime.now(),
                ))
        session.commit()
