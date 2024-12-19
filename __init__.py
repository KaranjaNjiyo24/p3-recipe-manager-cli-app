from models import Base
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///recipes.db"
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")