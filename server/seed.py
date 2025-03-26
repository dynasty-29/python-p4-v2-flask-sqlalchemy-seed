#!/usr/bin/env python3
#server/seed.py
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    # Create and initialize a faker generator
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    # Add some Pet instances to the list
    pets.append(Pet(name = "Fido", species = "Dog"))
    pets.append(Pet(name = "Whiskers", species = "Cat"))
    pets.append(Pet(name = "Hermie", species = "Hamster"))
    pets.append(Pet(name = "Slither", species = "Snake"))
    pets.append(Pet(name="Whiskers", species="Cat"))  
    pets.append(Pet(name="Chirpy", species="Parrot"))  
    pets.append(Pet(name="Bubbles", species="Fish"))  
    pets.append(Pet(name="Thumper", species="Rabbit"))  
    pets.append(Pet(name="Scurry", species="Hamster"))  

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()