'''
Predefined Functions = 2 types

1. Built in functions = already present in python 
2. Functions present inside the modules 

'''

#Built in Functions 

#EX_1 = Print function 

print("Hello World")
print ("hello","world") # "," helps to give space between the words.


print("Hello")
print("Python") # Two seperate lines are printed 

# End argument = default end argument is \n i.e., next line 

print("Hello", end=" ")
print("world")          #output = Hello World 

#sep argument = default seperator argument is space 

print("hello","python", sep = "@@")   #output = hello@@python

#EX_2 = Input function 

num = input("Enter a number: ")
print(num)



# Functions present in modules 

import math 
math.sqrt(5)
math.factorial(3)
print(math.sqrt(5))
