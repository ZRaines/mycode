#!/usr/bin/env python3

# Taking in a name as a parameter, and printing out the phrase "Hello <name>"

def inputname(your_name):
    print(f"Hello {your_name}")

inputname('Zakk')
inputname('Wade')

# Taking in a number as a parameter, printing out that number * 11, and returning that value.

def times_11(num):
    product = num * 11
    print(product)
    return product
times_11(3)
times_11(6)
my_num = int(input("What number should be multiplied by 11?"))
times_11(my_num)
