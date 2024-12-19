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

def add_user():
    session = Session()
    print("\n--- Add a New User ---")
    username = get_user_input("Username: ")
    email = get_user_input("Email: ", required=False)

    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()
    print(f"User '{username}' added successfully!\n")
    session.close()

def view_users():
    session = Session()
    print("\n--- All Users ---")
    users = session.query(User).all()

    if not users:
        print("No users found! Add some users first.\n")
        session.close()
        return

    print("ID\tUsername\tEmail")
    for user in users:
        print(f"{user.id}\t{user.username}\t{user.email or 'N/A'}")
    session.close()