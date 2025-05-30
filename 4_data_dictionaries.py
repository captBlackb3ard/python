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
dict1 = dict(name = "John", age = 18, country = "Kenya", gender = "Male")
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

#/**Dictionary Item Manipulation**/
print("\nDictionary Manipulation\n---------------------------------------------------------")
dict_car["year"] = 2018
print(f"\nChange the value of a specific dictionary item refer to its key name, e.g., dict_car['year'] = '2018' will return {dict_car.items()}")
dict1.update({"name":"Jonathan"})
print(f"\nAlterantively, use the update() method to change the value of a specific key, e.g., dict1.update('name':'Jonathan') will return {dict1.items()}")
dict_car["Drivetrain"] = "RWD"
print(f"\n To add a new item, add a new index/key and assign a value to it, e.g., dict_car['Drivetrain] = 'RWD' will retturn {dict_car.items()}")
dict_car.update({'fuel':'petrol'})
print(f"\nAlterantively, use the update() method to add a new item, e.g., dict_car.update('fuel':'petrol') will return {dict_car.items()}")
dict_car.pop('fuel')
print(f"\nUse the pop() method to remove an item key-value pair, e.g., dict_car.pop('fuel') will return {dict_car.items()}")
del dict_car['Drivetrain']
print(f"\nAlterantively, use the del keyword to remove and item key-value pair, e.g., del dict_car['Drivetrain'] will return {dict_car.items()}")
print(f"\nUsing the del keyword with no key specified will delete the entire dictionary, e.g., del dict_car")
dict_car.clear()
print(f"\nUsing the clear() method will empty the dictionary, e.g, dict_car.clear() will return a  dictionary with {len(dict_car)} items")
'''
Attempting to copy a dictionary dict2 = dict1 will only copy a reference to dict1 and any changes to dict1 will automatically be reflected in dict2
Instead use the following methods - copy() and dict()
'''
dict2 = dict1.copy() #dict2 will be a copy of dict1
dict3 = dict(dict1)  #dict3 will be a copy of dict1
print(f"\nUse the copy() method to create a copy of dictionary, e.g. dict2 = dict1.copy()")
print(f"Use the dict() method to create a copy of a dictionary, e.g, dict3 = dict(dict1)")

#/**Nested Dictionaries**/
dict_animal = {
    "animal1" : dict_hum,
    "animal2" : dict_wolf,
    "animal3" : dict_whale
}
print("\nNested Dictionaries\n---------------------------------------------------------")
print(f"\nDictionary dict_animal is a nested dictionary with {len(dict_animal)} items, but each item has {len(dict_animal['animal1'])} sub-items")
print(f"Dictionary dict_animal has the following key-value pairs {dict_animal.items()}")
for x, obj in dict_animal.items():
    print(f"\n{x} - ")

    for y in obj:
        print(y + ':', obj[y])
