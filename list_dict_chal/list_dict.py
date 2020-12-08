#!/usr/bin/env python3  
# List and Dictionary Challenge!
# 
# Create a list of dog names (at least 3)
# Create another list of cat names (at least 3)
# Append the cats list onto the dogs list (so it is a single list)
# Print out the first dog name from your single list
# Print out the second cat name from your single list
# Create a dictionary with the keys "first_dog" and "second_cat".
# Use the appropriate values from your list as the values for the dictionary keys
# Print out the dictionary
# Print out the value of "first_dog" and "second_cat" from the dictionary

dogs = ["Cheyenne", "Bailey", "Zeke"]

cats = ["Wiggles", "Kiwi", "Midnight"]

print(dogs)

dogs.append(cats)
print(dogs)
print(dogs[0])
print(cats[1])

dogs1 = {"first_dog": "Cheyenne", "second_cat": "Kiwi"}
print(dogs1)
print(dogs1.values())

