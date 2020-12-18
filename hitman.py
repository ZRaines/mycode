#!/usr/bin/env python3

""" Hitman Project | Author: Zakkary Raines """

import time
import crayons
from sys import exit as ex


mission = ""
database = ""
passwd = ""
round = 0

print("Welcome back Agent 47.")
time.sleep(1)
print("I hope your last mission was a success.")
time.sleep(2)

while round < 3 or mission.lower != "yes" or "no":
    round += 1
    mission = input("Are you ready for another contract?")
    if mission.lower() == "yes":
        print("Alright then, log into the database and see who's available.")
        break
    elif round == 3:
        print("Poor connection, disconnecting for security purposes.")
        ex()
    elif mission.lower() == "no":
        print("Perhaps another time then.")
        ex()
    else:
        print("Sorry I didn't catch that.")        

while round < 5 and database != "Agent 47":
    round += 1
    database = input("Username:")
    if database == "Agent 47":
        print("Authorized User, enter your password.")
    elif round == 5:
        print("Could not validate user, ending transmission")
        ex()
    else:
        print("Invalid Username. Insert a valid Username.")

while round < 6 and passwd != "ghost":
    round += 1
    passwd = input("Password:")
    if passwd == "ghost":
        print(crayons.green('Access Granted'))
    elif round == 6:
        print(crayons.red('ACCESS DENIED!!! Agent may be compromised. Goodbye.'))
    else:
        print("Incorrect password. Try again.")
