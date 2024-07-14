# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:52:13 2024

@author: Julian Nguyen
"""

# Write a program that asks the user to input 10 integers, and then 
# prints the largest odd number that was entered. If no odd number was entered,  
# it should print a message to that effect

#a placeholder to store the largest odd number found during the loop iterations.
#Initialize y to None to signify no odd number has been found yet
largest_odd = None

for number in range (10):
    # Enter 10 numbers 
    number = int (input("Enter an integer: "))
    # Check condition if number is odd 
    if (number%2 == 1):
        # Update y if it is the first odd number or if x is greater than the current y
        if largest_odd is None or number > largest_odd:
            # Update largest odd if condition is true
            largest_odd = number
        
# Print this message if No odd number was updated if the test fail
if largest_odd is None:
    print ("No odd number was entered")
# Print this message if largest odd was found 
else:
    print("Largest odd number is ", largest_odd)





# This version can only work for positive integer. If you initialize 0 to largest number -> get error bc cannot compare none to int 
### largest_odd = 0
### for counter in range(10):
###     number = int(input("Enter a number: "))
###     if (number % 2 == 1 and number > largest_odd):
###         largest_odd = number

### if (largest_odd == 0):
###     print("All are even")
### else:
###     print(largest_odd, "is the largest odd number")
