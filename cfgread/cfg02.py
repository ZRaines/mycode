#!/usr/bin/env python3

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
## create file object in "r"ead mode
configfile = open(f"{dir_path}/vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

## Always close your file
configfile.close()

