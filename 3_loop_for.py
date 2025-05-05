#!/usr/bin/python3

"""
For loops are used to iterate over a sequence - list, tuple, dictionary, set, or string
The 'for' loop does not require a indexing variable to beforehand
"""

#Simple for loop
fruits = ["apple", "banana", "cherry"]
print(f"List variable 'fruit' defined with values {fruits}")
print("\nUsing simple 'for' loop to iterate over the list:")
for x in fruits:
  print(x)

#Looping through a string
print("\nIt is possible to 'for' loop through each character in a string:")
for x in "Cheetah":
  print(x)

#Use the 'break' statement to stop a loop before looping through all the items
print("\nUse the 'break' statement to exit a loop prematurely (compare with first for loop above)")
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#Use the 'continue' statement to skip the current iteration and move on to the next
print("\nUse the 'continue' statement to skip the current iteration (compare with first for loop)")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The 'pass' statement is used when the for loop is empty (not supported)
for x in [0, 1, 2]:
  pass #Used to avoid getting an error 

#Use the range() emthod to loop through code a specificied number of times.
print("\nUse the 'range()' method to loop code a set number of times.")
print("Executing 'for x in rangeg(6)' generates (starting at '0')")
for x in range(6): #Defaults starts counting at '0' with a default increment of '1'
  print(x)

print("Executing 'for x in rangeg(2, 6)' generates (starting at '2')")
for x in range(2, 6):
  print(x)

print("Executing 'for x in rangeg(2, 30, 3)' generates (starting at '2' with an increment of '3')")
for x in range(2, 30, 3):
  print(x)


#'else' statement specifies a block of code to be executed when the loop is finished
print("\nCombining the 'else' keyword with a for loop will execute code when iteration is completed")
for x in range(6):
  print(x)
else:
  print("Looping finished!")
#'else' block will NOT be executed if the loop is stopped by a break statement.

#Nested loops - inner loop is executed for each outer loop iteration
print("\nExecuting nested loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    if y == "banana" and x == "red":
      print("yellow", y)
    else:
      print(x, y)