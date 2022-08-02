print("Welcome to the day trip genterator. I will assist you in deciding what trip you will be taking!")


# list of destinations
destination = ['Los Angeles', 'Philadelphia', 'San Diego', 'New York City']

transportation = ['plane', 'train', 'car', 'bus']

entertainment = ['movies', 'bowling', 'sight seeing', 'museum']

dinner = ['steak dinner', 'pizza parlor', 'seafood broil', 'sushi']

from operator import truediv
import random
from tkinter import Y

# print(f"How does {random.choice(destination)} sound?")

FLAG = True
while FLAG:
    print(f"How does {random.choice(destination)} sound?")
    user_choice = input("Enter y/n: ")
    if user_choice == "y":
        FLAG = False
    else:
        continue

print("Awesome next lets select your transportation!")
    
FLAG = True
while FLAG:
    print(f"How does a {random.choice(transportation)} sound?")
    user_choice = input("Enter y/n: ")
    if user_choice == "y":
        FLAG = False
    else:
        continue

print("Great! We're going to choose some entertainment next.")

FLAG = True
while FLAG:
    print(f"Does {random.choice(entertainment)} sound good to you?")
    user_choice = input("Enter y/n: ")
    if user_choice == "y":
        FLAG = False
    else:
        continue

print("Perfect! One more thing and we're finished. Time to choose your dining options.")

FLAG = True
while FLAG:
    print(f"How does {random.choice(dinner)} sound?")
    user_choice = input("Enter y/n: ")
    if user_choice == "y":
        FLAG = False
    else:
        continue

print("Great news, your day trip has been completed lets give you a rundown of what you'll be doing.")

print(f"For your destination you will be going to {(destination)}.")
