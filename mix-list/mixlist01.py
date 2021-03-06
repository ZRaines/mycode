#!/usr/bin/env python3

# create a list containing three items
my_list = ["192.168.0.5", 5060, "UP"]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

# create a new list of values
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# .format() method
#easy = "When I {} into IP addresses {} or {} I am unable to ping ports {}, {}, or {}." .format (new_list[5], new_list[3], new_list[4], new_list[0], new_list[1], new_list[2])
#print(easy)

# f-string approach
#easier = f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}."
#print(easier)

# .format() method IMPROVED!!!
easiest = "When I {5} into IP addresses {3} or {4} I am unable to ping ports {0}, {1}, or {2}." .format(*new_list)
print(easiest)        
 
# split into multi-line for readability
# Concatenation way
#print("When I ssh into IP addresses: " + new_list[3] )
#print("or " + new_list[4] + " I am unable to ping ports")
#print(str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]))


