import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

class DatabaseSessionSingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance

class DatabaseSession(Session, metaclass=DatabaseSessionSingletonMeta):
    def __init__(self):
        self.engine = create_engine(
            get_postgres_uri(),
            isolation_level="REPEATABLE READ",
        )
        super().__init__(bind=self.engine)
