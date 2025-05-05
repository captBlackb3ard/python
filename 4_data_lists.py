#!/usr/bin/python3

"""
Python has 4 built-in data types - Lists, Tuples, Sets, and Dictionary
"""

"""
=====================================================================
Lists
=====================================================================
Used to store multiple items in a single variable
Lists are defined as objects with the data type 'list
Lists are created using square brackets []
List items can be of any data type - string, int, Boolean, etc.
List items are ordered, changeable, and allow duplicate values
The order of list items cannot be changed - new items are added at the end of the list
List items are indexed, starting at [0]
"""

print("\nLists\n---------------------------------------------------------")
frstlist = ["apple", "banana", "cherry"]
print(f"The list frstlist is of type: {type(frstlist)}")
print(f"List variable 'frstlist' defined with values {frstlist}")
print(frstlist)

scndlist = ["apple", "banana", "cherry", "apple", "cherry"]
print(f"\nLists allow duplicate values: {scndlist}")

print(f"\nUse the 'len()' method to determine the number of list items: {len(scndlist)}")

thrdlist = ["abc", 34, True, 40, "male"]
print(f"\nLists can contain a different data types: {thrdlist}")

print("\nUse the list() method to create lists")
frthlist = list(("ape", "bear", "cheetah")) # note the double round-brackets
print(frthlist)

print(f"\nList items can accessed directly by using their index number, e.g., frstlist[1] will return {frstlist[1]}")
print(f"Negative indexing also works, e.g., frstlist[-1] will return {frstlist[-1]}")
print(f"It is possible to use a range of indexes, e.g., scndlist[1:4] will return {scndlist[1:4]}")