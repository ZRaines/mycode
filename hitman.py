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
        ex()
    else:
        print("Incorrect password. Try again.")

print("Now that you are logged in, you can view our open contracts.")
time.sleep(1)
print("------- Pulling up available targets -------")
time.sleep(2)

target1 = {"Name": "Viktor Novikov", "Location": "Serbia", "Payout": "500,000"}
target2 = {"Name": "Silvio Caruso", "Location": "Columbia", "Payout": "200,000"}
target3 = {"Name": "Francesca De Santis", "Location": "Northern France", "Payout": "2,000,000"}
target4 = {"Name": "Reza Zaydan", "Location": "Miami", "Payout": "250,000"}
target5 = {"Name": "General Makarov", "Location": "St. Petersburg", "Payout": "300,000"}

print(f"Name: {target1['Name']}")
print(f"Location: {target1['Location']}")
print(f"Payout: {target1['Payout']}")
print("-------------------")
print(f"Name: {target2['Name']}")
print(f"Location: {target2['Location']}")
print(f"Payout: {target2['Payout']}")
print("-------------------")
print(f"Name: {target3['Name']}")
print(f"Location: {target3['Location']}")
print(f"Payout: {target3['Payout']}")
print("-------------------")
print(f"Name: {target4['Name']}")
print(f"Location: {target4['Location']}")
print(f"Payout: {target4['Payout']}")
print("-------------------")
print(f"Name: {target5['Name']}")
print(f"Location: {target5['Location']}")
print(f"Payout: {target5['Payout']}")

while True:
    target = input("Do any of these jobs look appealing?")
    if target == "Viktor Novikov":
        print("You've chosen Viktor Novikov.")
        break
    elif target == "Silvio Caruso":
        print("You've chosen Silvio Caruso.")
        break
    elif target == "De Santis":
        print("You've chosen Francesca De Santis.")
        break
    elif target == "Reza Zaydan":
        print("You've chosen Reza Zaydan.")
        break
    elif target == "Makarov":
        print("You've chosen General Makarov.")
        break
    elif target.lower() == "no":
        print("We'll have new contracts next week. See you then.")
        ex()
    else:
        print("Pick one or wait until more contracts come available.")
        continue

pistol = ["Beretta Cougar", "HWK21", "Ruger MK II", "Ballers", "Desert Eagle" ]
rifle = ["M4A1", "WA2000", "Dragunov", "M14", "L96A1"]
woo = ["Fiber Wire", "Poison Syringe", "Tazer"]

print("Excellent. Now that you have a target, the fun can begin.")
time.sleep(2)
print("It's time for you to head to the armory and choose your weapons.")
time.sleep(2)
print("You'll be able to take one pistol, one rifle, and of course one specialty weapon.")
time.sleep(2)
print("We will begin with your pistol. Take a look at your choices.")
time.sleep(2)
print(pistol[0], '\n',  pistol[1], '\n', pistol[2], '\n', pistol[3], '\n', pistol[4])
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
print("Now you get to pick your big gun.")
time.sleep(2)
print("Our current rifle inventory consists of:")
time.sleep(1)
print(rifle[0], '\n',  rifle[1], '\n', rifle[2], '\n', rifle[3], '\n', rifle[4])
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

print("Last but not least, for when you want to get up close and personal.")
time.sleep(2)
print("Here are your special weapons.")
time.sleep(2)
print(woo[0], '\n',  woo[1], '\n', woo[2])
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
print("Looks like your all set.")
time.sleep(2)
print("Good luck. And remember, if you're compromised, we don't exist.")
