#!/usr/bin/python3

"""
Python functions are similar to other programming language functions
 - A block of code that only executes when called.
 - Pass data known as variables to the function for processing
 - Return data as a result
"""

#/**Function Definition**/
#/**----------------------------------------------------------------------
# Use the 'def' keyword to define a function
def hello_function():
    print("This Python function says Hello!")

#/**Function Arguments**/
#/**----------------------------------------------------------------------
# Functions can receive data as arguments
def arg_function(fname):
    print(f"Welcome {fname} to Python function programming.")

def argdefault_function(hereos = "Avengers"):
    print(f"The most interesting hero series is {hereos}")

def args_function(fname, lname):
    print(f"Please note {fname} {lname}, functions can receive more than one argument")

# Use '*' when it is not known how many arguments a function will receive
# The function will receive a tuple of arguments
def args2_function(*vals):
    print(f"Everyones favourite Avenger is {vals[2]}")

# Python functions can also receive arguments with key-value pairs
def argpair_function(arg1, arg2, arg3):
    print(f"The second favourite Avenger is {arg2}")

# Functions can receive any data type, including lists
def arglist_function(my_list):
    print("\nBelow is a list of a few of the Avengers:")
    for x in my_list:
        print("\t" + x)

# Use the 'pass' keyword to define an empty function
def empty_function():
    pass

#/**Function Results**/
#/**----------------------------------------------------------------------
# Use the 'return' keyword return a result from the function
def add_function(x, y):
    return x + y

#/**Recursion**/
#/**----------------------------------------------------------------------
def tri_recursion(k):
  if(k > 0):
    print(f"Orginal value - {k}")
    result = k + tri_recursion(k - 1)
    print(f"new value - {k}")
    print(result)
  else:
    result = 0
  return result





'''
Function Argument vs Parameter
Argument - data variable passed to a function
Parameter - data variable inside a function
'''

# Call ('Execute') a function
print("\nPython Function Execution\n---------------------------------------------------------")
hello_function()
arg_function("John")
argdefault_function() #Default argument used
argdefault_function("Marvel") #Alternative argument used for same function
args_function("Peter", "Parker")
args2_function("Hawk Eye", "Hulk", "Iron Man", "Spider Man", "Thor")
argpair_function(arg1="Thor", arg2="Spider Man", arg3="Hulk")

avengers = ["Iron Man - Tony Stark", "Spider Man - Peter Parker", "Captain America - Steve Rogers", "Black Widow - Natasha Romanoff", "Hulk - Bruce Banner"]
arglist_function(avengers)

print(f"\nThe sum of the two values x = 2 and y = 10 is: {add_function(2, 10)}")

print("\nRecursion Example Results:")
tri_recursion(6)