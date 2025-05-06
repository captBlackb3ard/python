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
print(f"\nUse the 'len()' method to determine the number of tuple items: {len(tuple2)}")
#Tuples with one item will need a comma added, else Python will not recognize it as a tuple
tuple0 = ("apple", )
print(f"tuple0 has only one item {tuple0}")
#Tuples can contain multiple data types
tuple3 = ("abc", 34, True, 40, "male")
print(f"\nTuples can contain a different data types: {tuple3}")
#Use the tupple() constructor to create a tuple
tuple4 = tuple(("alligator", "bear", "cheetah", "donkey"))
print(f"Use the 'tuple()' constuctor to create a tuple - {tuple4}")