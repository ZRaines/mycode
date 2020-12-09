#!/usr/bin/env python3


anime = '"Naruto", "7 Deadly Sins", or "One Punch Man"'
shows = input("Which anime should I watch?")

if shows == "I don't watch anime.":
    print("So what do you watch?")
    print("I prefer game shows.")
elif shows == "Let me think.":
    print("There are so many good anime, I recommend"  + anime)
else:
    print("Are you ignoring me?")

     
