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
#/**List Definition**/
print("\nList Definition\n---------------------------------------------------------")
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

#/**Accessing List Items**/
print("\nAccessing List Items\n---------------------------------------------------------")
print(f"List items can accessed directly by using their index number, e.g., frstlist[1] will return {frstlist[1]}")
print(f"Negative indexing also works, e.g., frstlist[-1] will return {frstlist[-1]}")
print(f"It is possible to use a range of indexes, e.g., scndlist[1:4] will return {scndlist[1:4]}")
print(f"Use the 'in' keyword to determine if an item exists in a list, e.g., 'if apple in frstlist'")
if "apple" in frstlist:
    print("'apple' is in the fruit list")

#/**List Item Manipulation**/
print("\nList Item Manipulation\n---------------------------------------------------------")
scndlist[3] = "dewberry"
print(f"To change the value of a specific list item refer to the index number, e.g., scndlist[3] = 'dewberry' will return {scndlist}")
thrdlist[1:3] = ["baboon", "chimpanzee"]
print(f"It is possible to change the value of a range of items using 'thrdlist[1:3]' syntax {thrdlist}")
frthlist.insert(2, "cow")
print(f"Use the 'insert()' method to add an item at a specific index, e.g., frthlist.insert(2) will return {frthlist}")
frthlist.append("deer")
print(f"Use the 'append()' method to add an item at the end of the list, e.g., frthlist.append('value') will return {frthlist}")
frthlist.remove("cow")
print(f"Use the 'remove()' to delete a specific list item by value, e.g., frthlist.remove('cow') results in {frthlist}") #Only removes the first occurrence
frthlist.pop(1)
print(f"The 'pop()' method removes a specified index, e.g., frthlist.pop(1) results in {frthlist}") #The last item is removed if no index is specified
del scndlist[4]
print(f"Use the 'del' keyword to delete a specified index value, e.g, del scndlist[4] results {scndlist}")
print(f"Running 'del scndlist' will delete the list completely.")
frstlist.clear()
print(f"Use the 'clear()' method to empty a list, e.g., frstlist.clear() results in an empty list {frstlist}")
fruitlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(f"Use the 'sort()' method to alphanumerically ascending sort this list {fruitlist}")
fruitlist.sort()
print(f"Execute fruitlist.sort() will return {fruitlist}")
print("Use fruitlist.sort(reverse = True) to sort in descending order")
#Use the copy() method to copy lists
foodlist = fruitlist.copy()
print(f"foodlist is a copy of the fruitlist - {foodlist}")
print("\nUse the 'extend()' method to join two lists")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
print(f"List 1 - {list1} and List 2 - {list2}")
list1.extend(list2)
print(f"Joined lists {list1}")
#Creating a list of fruits that contain 'a' in the name using List Compression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(f"List compression created list {newlist}")