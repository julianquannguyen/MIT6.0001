# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:59:16 2024

@author: Julian Nguyen
"""

# Let s be a string that contains a sequence of decimal numbers 
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the 
# sum of the numbers in s.

s = input('Enter a sequence of decimal numbers separated by commas: ')
# use this s = 1.23,2.4,3.123 to refer to the comment section in the code 
total = 0
temp_str = ''

for i in s:
    # Evaluate each character in s. If character is not ',' it will be added to temp_str
    if (i!= ','):
        temp_str += i
        # Output will be like this if using print(temp_str)
        # 1
        # 1.
        # 1.2
        # 1.23
        # 1.232
        # 1.232.
        # 1.232.4
        # 1.232.43
        # 1.232.43.
        # 1.232.43.1
        # 1.232.43.12
        # 1.232.43.123
    
    # Else is to handle when character is ','. ',' indicate it is the end of number
    # if dont have else statement there will be error for when convert string to float & add it back to total
    else:
        total += float(temp_str)
        temp_str = ''
        # if character is ','. Convert all accumulated string to float and add it back to total.
        # Then reset the temp_str back to '' to use for next number
        # Output will be 3.63
        
# this is use to handle last number when there is no ','
total += float(temp_str) # Output = 6.753
print ('Sum of the sequence is ', total)