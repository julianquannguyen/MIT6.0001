# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:07:10 2024

@author: Julian Nguyen
"""

# Replace the comment in the following code with a while loop.
###         numXs = int(input('How many times should I print the letter X? '))
###         toPrint = ''
###         #concatenate X to toPrint numXs times
###         print(toPrint)



numXs = int(input('How many times should I print the letter X? '))
toPrint = ''

if numXs < 1:
    print ("Value of numXs is less than or equal to zero")
else:
    while(numXs > 0):
        toPrint += 'X'
        numXs -= 1
    print(toPrint)