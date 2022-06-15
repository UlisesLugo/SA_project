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
    Text,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)


def start_mappers():
    Base.metadata.create_all(engine)
    
    with sessionmaker(bind=engine)() as session:
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
