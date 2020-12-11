#!/usr/bin/env python3

def inputname(your_name):
    print(f"Hello {your_name}")
def timeseleven(num):
    print(f"The value returned is {num * 11}")
def main():
    firstname = input("What is your name?")
    inputname(firstname)
    value = input("Which number do you want to use?")
    timeseleven(value)
main()
