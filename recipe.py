import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models1 import Base, User, Recipe, Ingredient, RecipeIngredient

DATABASE_URL = "sqlite:///recipes.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_database():
    if not os.path.exists("recipes.db"):
        Base.metadata.create_all(engine)
        print("Database created successfully!")
