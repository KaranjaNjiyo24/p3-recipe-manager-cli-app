import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Recipe, Ingredient, RecipeIngredient

DATABASE_URL = "sqlite:///recipes.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

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

def add_recipe():
    session = Session()
    print("\n--- Add a New Recipe ---")
    
    # Select User
    users = session.query(User).all()
    if not users:
        print("No users found! Add a user first.\n")
        session.close()
        return

    print("Select a User by ID:")
    for user in users:
        print(f"{user.id}: {user.username}")
    user_id = get_user_input("User ID: ", input_type=int)

    user = session.query(User).get(user_id)
    if not user:
        print("Invalid User ID.\n")
        session.close()
        return

    # Collect recipe details
    name = get_user_input("Recipe Name: ")
    description = get_user_input("Description (optional): ", required=False)
    prep_time = get_user_input("Preparation Time (in minutes): ", input_type=int)
    cook_time = get_user_input("Cooking Time (in minutes): ", input_type=int)
    servings = get_user_input("Number of Servings: ", input_type=int)

    # Add ingredients
    print("\n--- Add Ingredients ---")
    ingredients = []
    while True:
        ingredient_name = get_user_input("Ingredient Name (or type 'done' to finish): ", required=False)
        if ingredient_name.lower() == 'done':
            break
        quantity = get_user_input("Quantity: ", input_type=float)
        unit = get_user_input("Unit: ")

        # Check if ingredient already exists
        ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
        if not ingredient:
            ingredient = Ingredient(name=ingredient_name)
            session.add(ingredient)
            session.commit()

        ingredients.append({"ingredient": ingredient, "quantity": quantity, "unit": unit})

    # Save recipe to the database
    new_recipe = Recipe(name=name, description=description, prep_time=prep_time, cook_time=cook_time, servings=servings, user=user)
    session.add(new_recipe)
    session.commit()

    for item in ingredients:
        recipe_ingredient = RecipeIngredient(
            recipe_id=new_recipe.id,
            ingredient_id=item["ingredient"].id,
            quantity=item["quantity"],
            unit=item["unit"]
        )
        session.add(recipe_ingredient)

    session.commit()
    print(f"Recipe '{name}' added successfully!\n")
    session.close()

def view_recipes():
    session = Session()
    print("\n--- All Recipes ---")
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes found! Add some recipes first.\n")
        session.close()
        return

    print("ID\tName\tPrep Time\tCook Time\tServings\tUser")
    for recipe in recipes:
        user = recipe.user.username if recipe.user else "N/A"
        print(f"{recipe.id}\t{recipe.name}\t{recipe.prep_time}\t{recipe.cook_time}\t{recipe.servings}\t{user}")
    session.close()

def view_ingredients():
    session = Session()
    print("\n--- All Ingredients ---")
    ingredients = session.query(Ingredient).all()

    if not ingredients:
        print("No ingredients found!\n")
        session.close()
        return

    print("ID\tName")
    for ingredient in ingredients:
        print(f"{ingredient.id}\t{ingredient.name}")
    session.close()

def view_recipe_details():
    session = Session()
    print("\n--- View Recipe Details ---")
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found! Add some recipes first.\n")
        session.close()
        return

    print("Select a Recipe by ID:")
    for recipe in recipes:
        print(f"{recipe.id}: {recipe.name}")

    recipe_id = get_user_input("Recipe ID: ", input_type=int)
    recipe = session.query(Recipe).get(recipe_id)
    if not recipe:
        print(f"Recipe with ID {recipe_id} not found.\n")
        session.close()
        return

    print(f"\nRecipe Name: {recipe.name}")
    print(f"Description: {recipe.description or 'No description provided'}")
    print(f"Preparation Time: {recipe.prep_time} minutes")
    print(f"Cooking Time: {recipe.cook_time} minutes")
    print(f"Servings: {recipe.servings}")
    print(f"Created By: {recipe.user.username}")
    print("\nIngredients:")
    print("Ingredient Name\tQuantity\tUnit")
    for recipe_ingredient in session.query(RecipeIngredient).filter_by(recipe_id=recipe.id).all():
        ingredient = session.query(Ingredient).get(recipe_ingredient.ingredient_id)
        print(f"{ingredient.name}\t{recipe_ingredient.quantity}\t{recipe_ingredient.unit}")
    session.close()

# Main CLI Function
def main():
    create_database()
    while True:
        print("\n--- Recipe Manager CLI ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Add Recipe")
        print("4. View Recipes")
        print("5. View Ingredients")
        print("6. View Recipe Details")
        print("7. Exit")
        choice = get_user_input("Choose an option: ", input_type=int)

        if choice == 1:
            add_user()
        elif choice == 2:
            view_users()
        elif choice == 3:
            add_recipe()
        elif choice == 4:
            view_recipes()
        elif choice == 5:
            view_ingredients()
        elif choice == 6:
            view_recipe_details()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
