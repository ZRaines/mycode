#!/usr/bin/env python3

# key: value
# basic dictionary = {"key": "value"}


my_car = {"year": 2015,  "color": "white",  "style": "Jetta"}
#print(type(my_car))
#print(my_car)
print(f"I drive a {my_car['year']} {my_car['color']} {my_car['style']}")


myform = {"name": "Zakk", "State": "VA"}
print(myform)
print(f"My name is {myform['name']} and I live in {myform['State']}")
print(my_car.get('year'))
print(my_car.keys())
print(my_car.values())

print(my_car.items())
