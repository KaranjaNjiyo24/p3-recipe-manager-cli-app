# **Recipe Manager CLI Application**

## **Introduction**
Welcome to the Recipe Manager CLI — a powerful yet simple tool designed to help you manage recipes and ingredients efficiently. Whether you're a culinary enthusiast or a professional chef, this application ensures your recipes are organized, accessible, and easy to use.

With a Kenyan culinary touch, you can document popular local dishes like **Nyama Choma**, **Pilau**, or **Ugali with Sukuma Wiki**, complete with their ingredients and preparation steps.

---

## **Features**
### 🧑‍🍳 **User Management**
- Create users to manage their own recipes.
- View a list of all registered users.

### 🍽️ **Recipe Management**
- Add new recipes with detailed descriptions and preparation information.
- View all saved recipes.
- View specific recipe details, including ingredients.

### 🥗 **Ingredient Management**
- Add ingredients while creating recipes.
- View a comprehensive list of all ingredients.
- Link ingredients to multiple recipes using a shared pool.

### 🔗 **Relationship Management**
- Easily explore the connection between recipes and their ingredients.
- Avoid duplication by reusing common ingredients (e.g., salt, onions).

---

## **Installation**

### **Requirements**
- Python 3.8+
- `pip` package manager
- `pipenv` package manager

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/KaranjaNjiyo24/p3-recipe-manager-cli-app.git
   cd p3-recipe-manager-cli-app
   ```

2. Initialize the database:
   ```bash
   python recipe.py
   ```

---

## **Usage**

### **Main Menu**
Once you run the application, you’ll be greeted with the main menu:
```
--- Recipe Manager CLI ---
1. Add User
2. View Users
3. Add Recipe
4. View Recipes
5. View Ingredients
6. View Recipe Details
7. Exit
```

### **Sample Workflow**
1. **Add a User**: Create users to own recipes (e.g., John or Jane).
2. **Add a Recipe**: Add recipes like "Nyama Choma" or "Pilau," linking them to users.
3. **View Recipes**: See all saved recipes or drill down to view specific details.
4. **View Ingredients**: Explore all ingredients used across recipes.
5. **View Recipe Details**: Examine the relationship between recipes and their ingredients.

---

## **Kenyan Context**
This application is tailored for my rich Kenyan cuisine but is flexible enough to manage recipes from any culture. Some examples included:
- **Nyama Choma**: Grilled meat with lemon and salt.
- **Pilau**: Spiced rice dish with Pilau Masala.
- **Ugali with Sukuma Wiki**: A traditional maize meal served with greens.

---

## **Technology Stack**
- **Python**: Core programming language.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite**: Lightweight database for storing recipes and ingredients.

---

## **Database Structure**
### **Models**
1. **User**: Tracks individual users managing recipes.
2. **Recipe**: Represents a single recipe, linked to a user.
3. **Ingredient**: Stores unique ingredients used in recipes.
4. **RecipeIngredient**: Association table linking recipes to ingredients, including `quantity` and `unit`.

### **Relationships**
- **One User → Many Recipes**
- **One Recipe ↔ Many Ingredients** (via `RecipeIngredient` table)
- **One Ingredient ↔ Many Recipes**

---

## **Future Enhancements**
- 🛠️ Export recipes to PDF or text file.
- 🌐 Add support for web or mobile integration.
- 📊 Analytics to show ingredient usage trends.

---

## **License**
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## **Contributors**
- **Karanja Njiyo** - Developer and Kenyan food enthusiast 🍲
- Open to contributions! 

---

## **Contact**
For feedback, please contact:
- Email: karanjaandrew2000@gmail.com
