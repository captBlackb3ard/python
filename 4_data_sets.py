#!/usr/bin/python3

"""
Python has 4 built-in data types - Lists, Tuples, Sets, and Dictionary
"""

"""
=====================================================================
Sets
=====================================================================
Used to store multiple items in a single variable
Sets are a collection of unordered, unchangeable, and unindexed values
Sets are created using curly brackets {}
Sets DO NOT allow duplicate values
"""

#/**Set Definition**/
print("\nSet Definition\n---------------------------------------------------------")
set1 = {"alligator", "bear", "cheetah", "deer"}
print(f"The set set1 is of type: {type(set1)}")
print(f"Set variable 'set1' defined with values {set1}")
set2 = ("abc", 34, True, 40, "male")
print(f"Sets can contain a different data types: {set2}")
print(f"\nUse the 'len()' method to determine the number of set items in set1: {len(set1)}")
#Use the set() constructor to create a set
set3 = set(("alligator", "bear", "cheetah", "deer"))
print(f"Use the 'set()' constuctor to create a tuple - {set3}")


#/**Accessing Set Items**/
print("\nAccessing Set Items\n---------------------------------------------------------")
print("Set items cannot be accessed by index; instead use iteration")
i = 0
for x in set3:
    print(f"Item {i} - {x}")
    i+=1
#Check if value/item is present in set
print("bear" in set3) #Returns boolean true
print("elephant" not in set3)  #Returns boolean true
print("elephant" in set3)  #Returns boolean false

#/**Set Item Manipulation**/
print("\nSet Item Manipulation\n---------------------------------------------------------")
print("Tuples are immutable - cannot be changed once set")
set3.add('elephant')
print(f"\nUse the 'add()' method to add an item to a set, e.g., set3.add('elephant') returns {set3}")
print("\nSets can be added (joined) to tuples using the 'update()' method")
set4 = {"apple", "banana", "cherry"}
set5 = {"pineapple", "mango", "papaya"}
print(f"Before 'joining' set4 - {set4} and set5 - {set5}")
set4.update(set5)
print(f"Final joined set4 - {set4}")
print("The 'update()' method can be used to join sets to lists or dictionaries")
set4 = {"apple", "banana", "cherry"}
list1 = ["kiwi", "orange"]
print(f"Before 'joining' set4 is of type {type(set4)} and list1 is of type {type(list1)}")
set4.update(list1)
print(f"Final set after joining a list {set4}")
print("\nUse the 'remove()' or 'discard()' methods to remove a set item")
set4.remove('banana')
print(f"Using set4.remove('banana') returns {set4}") #discard() will not generate an error if the item does not exist
set4.pop()
print(f"Use the 'pop()' method to remove a random item {set4}")
set4.clear()
print(f"Use the 'clear()' method to empty a set, e.g., set4.clear() results in an empty list {set4}")
print(f"Running 'del set3' will delete the set completely.")