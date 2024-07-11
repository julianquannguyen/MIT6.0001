# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 07:31:59 2024

@author: Julian Nguyen
"""

# Write a program that examines three variables—x, y, and z—and 
# prints the largest odd number among them. If none of them are odd, it should 
# print a message to that effect.

x = int(input("Enter number x = "))
y = int(input("Enter nymber y = "))
z = int(input("Enter number z = "))

if (x%2 != 0 and y%2 != 0 and z%2 !=0):
    if (x>y and x>z):
        print ("x is the largest odd number.")
    elif (y>x and y>z):
        print ("Y is the largest odd number.")
    else:
        print("z is the largest odd number.")
elif(x%2 != 0 or y%2 != 0 or z%2 !=0):
    print("x, y, z must be all odd numbers to compare largest number.")
else:
    print("No odd numbers to compare.")
