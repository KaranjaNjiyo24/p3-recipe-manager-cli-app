from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    recipes = relationship('Recipe', back_populates='user')

# Recipe Model
class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    prep_time = Column(Integer, nullable=False)
    cook_time = Column(Integer, nullable=False)
    servings = Column(Integer, nullable=False)

    user = relationship('User', back_populates='recipes')
    ingredients = relationship('Ingredient', secondary='recipe_ingredients', back_populates='recipes')