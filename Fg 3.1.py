# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 07:31:59 2024

@author: Julian Nguyen
"""

# Write a program that asks the user to enter an integer and prints 
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to 
# the integer entered by the user. If no such pair of integers exists, 
# it should print a message to that effect.

# # Get input from users
# i = int(input('Enter an integer: '))
# # Initialize pwr = 1 because pwr > 0
# pwr = 1
# # Set a vảiable to indicate you find the pair pwr**root = i
# found = False 
# # loop 1 to search all of the power from 0 - 6
# while pwr < 6:
#     # Initialize root = 0 to start search root for pwr
#     root = 0
#     # Loop 2 to search all possible root for pwr suitable the condition
#     while root ** pwr <= abs(i):
#         if root ** pwr == abs(i):
#             print('The root of number', i, 'is', root)
#             print('The power of number', i, 'is', pwr)
#             print (root,'**', pwr, '=' , root**pwr)
#             #indicate you found the pair to stop loop
#             found = True 
#         # increment root for loop 2 
#         root += 1
#     #incremnet pwr for loop 1 
#     pwr += 1

# # other condition if cannot find the pair
# if not found:
#     print ('No such pair of root and power exists for number', i)
        

 
# Different way use for loop to solve the problem
i = int(input('Enter an integer: '))
found = False 

#loop for value of power from 1-5
for pwr in range(1,6):
    #loop for ptential value of root of number
    for root in range (0, abs(i)+1):
      if root ** pwr == abs(i): 
          print('The root of number', i, 'is', root) 
          print('The power of number', i, 'is', pwr) 
          print (root,'**', pwr, '=' , root**pwr)
          #indicate you found the pair to stop loop
          found = True
      root += 1
pwr += 1
# other condition if cannot find the pair
if not found:
    print ('No such pair of root and power exists for number', i)
        
    
 

