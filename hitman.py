#!/usr/bin/env python3

""" Hitman Project | Author: Zakkary Raines """

import time
import crayons

round = 0
print("Welcome back Agent 47.")
time.sleep(1)
print("I hope your last mission was a success.")
time.sleep(2)
mission = input("Are you ready for another contract?")
while True:
    if mission.lower() == "yes":
        print("Alright then, log into the database and see what's available.")
        database = input("Username:")
        if database == "Agent 47":
            passwd = input("Password:")
            if passwd == "ghost":
               print(crayons.green('Access Granted', time)    
        elif database != "Agent 47":
        error = input("Username not recognized. Please insert a valid Username.")
        #passwd = input("Password:")
            elif mission.lower() == "no":
            print("Perhaps another time then.")
            break
    else:
        print("Sorry I didn't catch that. There may be interference on your end.")        

    
    #print(crayons.red('ACCESS DENIED!'))

#if database == "Agent 47":
    #print(crayons.green('Access granted', time.now()))

