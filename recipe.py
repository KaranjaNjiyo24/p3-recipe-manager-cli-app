import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models1 import Base, User, Recipe, Ingredient, RecipeIngredient

DATABASE_URL = "sqlite:///recipes.db"
engine = create_engine(DATABASE_URL)
session = Session()

def create_database():
    if not os.path.exists("recipes.db"):
        Base.metadata.create_all(engine)
        print("Database created successfully!")

def get_user_input(prompt, required=True, input_type=str):
    while True:
        user_input = input(prompt)
        if not user_input and required:
            print("This field is required. Please provide a value.")
            continue
        try:
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")