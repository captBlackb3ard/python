#!/usr/bin/python3

"""
Python has 4 built-in data types - Lists, Tuples, Sets, and Dictionary
"""

"""
Python has 4 built-in data types - Lists, Tuples, Sets, and Dictionary
"""

"""
=====================================================================
Tuples
=====================================================================
Used to store multiple items in a single variable
A tuple is ordered and unchangable (immutable)
Tuples are created using parentheses ()
Tuples allow duplicate values
Tuple items are indexed, starting at [0]
"""

#/**Tuple Definition**/
print("\nTuple Definition\n---------------------------------------------------------")
tuple1 = ("apple", "banana", "cherry")
print(f"The tuple tuple1 is of type: {type(tuple1)}")
print(f"Tuple variable 'tuple1' defined with values {tuple1}")
#tuple2 has duplicates
tuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(f"Tuples can contain duplicate values - {tuple2}")
print(f"\nUse the 'len()' method to determine the number of tuple items in tuple2: {len(tuple2)}")
#Tuples with one item will need a comma added, else Python will not recognize it as a tuple
tuple0 = ("apple", )
print(f"tuple0 has only one item {tuple0}")
#Tuples can contain multiple data types
tuple3 = ("abc", 34, True, 40, "male")
print(f"\nTuples can contain a different data types: {tuple3}")
#Use the tupple() constructor to create a tuple
tuple4 = tuple(("alligator", "bear", "cheetah", "donkey"))
print(f"Use the 'tuple()' constuctor to create a tuple - {tuple4}")


#/**Accessing Tuple Items**/
print("\nAccessing Tuple Items\n---------------------------------------------------------")
print(f"Tuples items can accessed directly by using their index number, e.g., tuple1[1] will return {tuple1[1]}")
print(f"Negative indexing also works, e.g., tuple1[-1] will return {tuple1[-1]}")
tuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"It is possible to use a range of indexes, e.g., tuple5[1:4] will return {tuple5[1:4]}")
print(f"Use the 'in' keyword to determine if an item exists in a tuple, e.g., 'if banana in tuple5'")
if "banana" in tuple5:
    print("'banana' is in the fruit tuple")


#/**Tuple Item Manipulation**/
print("\nTuple Item Manipulation\n---------------------------------------------------------")
#Tuples cannot be changed after creation - immutable
print("Tuples are immutable, but can be converted into lists, modified, and reverted back to a tuple")
list1 = list(tuple1)
list1.append("dewberry")
tuple1 = tuple(list1)
print(f"List converted {list1} and Tuple coverted (after list manipulation) {tuple1}") 
print("Tuples can be added (joined) to tuples using the '=+' operator")
tupley = ("elderberry", )
tuple1 += tupley
print(f"Final tuple1 after addition - {tuple1}")
print(f"Tuples can be multiplied using the '*' operator, e.g, {tuple0}*3 returns {tuple0*3}")