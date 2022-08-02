

print("Welcome to the day trip genterator. I will assist you in deciding what trip you will be taking!")


# list of destinations
destination = ['Los Angeles', 'Philadelphia', 'San Diego', 'New York City']

transportation = ['plane', 'train', 'car', 'bus']

entertainment = ['movies', 'bowling', 'sight seeing', 'museum']

dinner = ['steak dinner', 'pizza', 'seafood broil', 'sushi']

from operator import truediv
import random
from tkinter import Y

# print(f"How does {random.choice(destination)} sound?")
def random_destination_generator():
    FLAG = True
    while FLAG:
        randomly_selected_destination = random.choice(destination)
        print(f"How does {randomly_selected_destination} sound?")
        user_choice = input("Enter y/n: ")
        if user_choice == "y":
            FLAG = False
            return randomly_selected_destination

destination_selected = random_destination_generator()

print("Awesome next lets select your transportation!")

def random_transportation_generator():    
    FLAG = True
    while FLAG:
        randomly_selected_transportation = random.choice(transportation)
        print(f"How does a {randomly_selected_transportation} sound?")
        user_choice = input("Enter y/n: ")
        if user_choice == "y":
            FLAG = False
            return randomly_selected_transportation

transportation_selected = random_transportation_generator()           

print("Great! We're going to choose some entertainment next.")

def random_entertainment_generator():
    FLAG = True
    while FLAG:
        randomly_selected_entertainment = random.choice(entertainment)
        print(f"Does {randomly_selected_entertainment} sound good to you?")
        user_choice = input("Enter y/n: ")
        if user_choice == "y":
            FLAG = False
            return randomly_selected_entertainment

entertainment_selected = random_entertainment_generator()           

print("Perfect! One more thing and we're finished. Time to choose your dining options.")

def random_dinner_generator():
    FLAG = True
    while FLAG:
        randomly_selected_dinner = random.choice(dinner)
        print(f"How does {randomly_selected_dinner} sound?")
        user_choice = input("Enter y/n: ")
        if user_choice == "y":
            FLAG = False
            return randomly_selected_dinner

dinner_selected = random_dinner_generator()          

print("Great news, your day trip has been completed lets give you a rundown of what you'll be doing.")

print(f"For your destination you will be going to {destination_selected} traveling by {transportation_selected}. Your entertainment for the day will be {entertainment_selected} capping the night off with {dinner_selected} for your meal!")