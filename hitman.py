#!/usr/bin/env python3

""" Hitman Project | Author: Zakkary Raines """

import time
from sys import exit as ex
import crayons


print("Welcome back Agent 47.")
time.sleep(1)
print("I hope your last mission was a success.")
time.sleep(2)
#Defining function to decide on taking another contract
def contract():
    mission = ""
    database = ""
    passwd = ""
    round = 0
    while round < 3 or mission.lower != "yes" or "no":
        round += 1
        mission = input("Are you ready for another contract?")
        if mission.lower() == "yes":
            time.sleep(1)
            print("Alright then, log into the database and see who's available.")
            break
        elif round == 3: #If your answer isn't yes or no after 3 tries, disconnect
            print("Poor connection, disconnecting for security purposes.")
            ex()
        elif mission.lower() == "no":
            print("Perhaps another time then.")
            ex()
        else: #Print this message if answer is not yes or no
            print("Sorry I didn't catch that.")
    while round < 5 and database != "Agent 47":
        round += 1 #Increase the count for each incorrect input
        database = input("Username:")
        if database == "Agent 47":
            print("Authorized User, enter your password.")
        elif round == 5:#Once invalid inputs = 5, disconnect
            print("Could not validate user, ending transmission")
            ex()
        else:
            print("Invalid Username. Insert a valid Username.")
    while round < 6 and passwd != "ghost":
        round += 1
        passwd = input("Password:")
        if passwd == "ghost":
            print(crayons.green('Access Granted'))
        elif round == 6:#Deniy access once invalid inputs = 6
            print(crayons.red('ACCESS DENIED!!! Agent may be compromised. Goodbye.'))
            ex()
        else:
            print("Incorrect password. Try again.")

contract()

print("Now that you are logged in, you can view our open contracts.")
time.sleep(1)
print("------- Pulling up available targets -------")
time.sleep(2)
#Defining function to view and/or select a target
def targets():
    target = open("targets.txt", "r") # Pull info from corresponding file
    print(target.read())
    while True:
        target = input("Do any of these jobs look appealing?")
        if target.lower() == "viktor novikov":
            print("You've chosen Viktor Novikov.")
            break
        elif target.lower() == "silvio caruso":
            print("You've chosen Silvio Caruso.")
            break
        elif target.lower() == "de santis":
            print("You've chosen Francesca De Santis.")
            break
        elif target.lower() == "reza zaydan":
            print("You've chosen Reza Zaydan.")
            break
        elif target.lower() == "makarov":
            print("You've chosen General Makarov.")
            break
        elif target.lower() == "no":
            print("We'll have new contracts next week. See you then.")
            ex()
        else:
            print("Pick one or wait until more contracts come available.")
            continue
targets()

print("Excellent. Now that you have a target, the fun can begin.")
time.sleep(2)
print("It's time for you to head to the armory and choose your weapons.")
time.sleep(2)
print("You'll be able to take one pistol, one rifle, and of course one specialty weapon.")
time.sleep(3)
print("We will begin with your pistol. Take a look at your choices.")
time.sleep(3)
#Defining function to choose a pistol
def pistols():
    pistol = open("pistols.txt","r") #Pull info from corresponding file
    print(pistol.read())
    while True:
        w1 = input("So what will it be?")
        if w1.lower() == "beretta cougar":
            print("Not a bad option.")
            break
        elif w1.lower() == "hwk21":
            print("That's a new one, let us know how it shoots.")
            break
        elif w1.lower() == "ruger":
            print("Been awhile since that was used, might want to dust it off.")
            break
        elif w1.lower() == "ballers":
            print("Can't beat old reliable huh?")
            break
        elif w1.lower() == "desert eagle":
            print("A bit of overkill don't you think.")
            break
        else:
            print("We don't have that in stock.")
            continue
pistols()
time.sleep(2)
print("Now you get to pick your big gun.")
time.sleep(2)
print("Our current rifle inventory consists of:")
time.sleep(2)
#Defining function to select a rifle
def rifles():
    rifle = open("rifles.txt", "r") # Pull info from corresponding file
    print(rifle.read())
    while True:
        r1 = input("See any that you like?")
        if r1.lower() == "m4a1":
            print("Looking to have some fun I see.")
            break
        elif r1.lower() == "wa2000":
            print("Interesting choice.")
            break
        elif r1.lower() == "dragunov":
            print("Never knew you had a thing for Russians.")
            break
        elif r1.lower() == "m14":
            print("That's original Vietnam era, be careful.")
            break
        elif r1.lower() == "l96a1":
            print("They won't even know where the shot came from.")
            break
        else:
            print("What you see is what you get.")
            continue
rifles()
time.sleep(2)
print("Last but not least, for when you want to get up close and personal.")
time.sleep(2)
print("Here are your special weapons.")
time.sleep(2)
#Defining function to select a weapon of opportunity
def woo():
    woos = open("woo.txt", "r") # Pull info from corresponding file
    print(woos.read())
    while True:
        s1 = input("Last weapon before you're off. What will it be?")
        if s1.lower() == "fiber wire":
            print("Oof, that's a painful way to go.")
            break
        elif s1.lower() == "poison syringe":
            print("That's some fast acting stuff right there.")
            break
        elif s1.lower() == "tazer":
            print("Since when was non-lethal your style?")
            break
        else:
            print("We'll have more options in the future. For now just pick one.")
            continue
woo()
time.sleep(2)
print("Looks like your all set.")
time.sleep(2)
print("Good luck. And remember, if you're compromised, we don't exist.")
