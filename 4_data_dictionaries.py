#!/usr/bin/python3

"""
Python has 4 built-in data types - Lists, Tuples, Sets, and Dictionary
"""

"""
=====================================================================
Dictionary
=====================================================================
Used to store values in key:value pairs
Dictionaries are ordered, changeble (mutable), and DO NOT allow duplicates
Dictionaries are created using curly brackets {} and have key:value pairs
"""

#/**Dictionary Definition**/
print("\nDictionary Definition\n---------------------------------------------------------")
dict_hum = {
  "species": "sapiens",
  "genus"  : "homo",
  "family" : "homindae", 
  "order"  : "primates"
}

dict_wolf = {
  "species": "lupus",
  "genus"  : "canis",
  "family" : "canidae", 
  "order"  : "carnivora"
}

dict_whale = {
  "species": "musculus",
  "genus"  : "baleenoptera",
  "family" : "balaenidae", 
  "order"  : "cetacea"
}

dict_car = {
  "brand": "Ford",
  "model": "Mustang",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(f"The dictionary dict_hum is of type: {type(dict_hum)}")
print(f"Dictionary value for the species of 'dict_hum' key 'family' is: {dict_hum['species']}")
print(f"\nUse the 'len()' method to determine the number of dictionary items in dict_hum: {len(dict_hum)}")
print(f"\nDictionaries can contain different data types, e.g, the dict_car holds Electric: {dict_car['electric']}, Model:{dict_car['model']}, and Colors: {dict_car['colors']}")
#Use the dict() constructor to create a dictionary
dict1 = dict(name = "John", age = 36, country = "Kenya", gender = "Male")
print(f"Use the 'dict()' constuctor to create a dictionary - {dict1}")

#/**Accessing Dictionary Items**/
print("\nAccessing Dictionary Items\n---------------------------------------------------------")
print(f"Aside from using the key to retrieve values, use the 'get()' method, e.g, 'dict_car.get('brand')' returns {dict_car.get('brand')}")
print(f"\nThe 'keys()' method will return the list of all dictionary keys, e.g, 'dict_car.keys()' returns {dict_car.keys()} ")
print(f"\nThe 'values()' method will return the list of all dictionary values, e.g, 'dict_car.values()' returns {dict_car.values()} ")
print(f"\nThe 'items()' method will return each item in a dictionary as tuples in a list, e.g, 'dict_whale.items()' returns {dict_whale.items()}")
print(f"\nUse the 'in' keyword to determine if a specific key is present in a dictionary, e.g., 'if model in dict_car'")
if "model" in dict_car:
    print("'model' is a key in the car dictionary")

#/**Dictionary Manipulation**/
print("\nDictionary Manipulation\n---------------------------------------------------------")