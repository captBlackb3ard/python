#!/usr/bin/python3

"""
There are 3 numeric types in Python:
- int (integers)
- float 
- comple

Use the type() method to verify the object type
"""


a = "Hello World"
b = 20
c = 20.5
d = 1j
e = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print("\nVariable Definitions\n---------------------------------------------------------")
print(f"The variable 'a' has been assigned the string value 'Hello World' i.e. 'a = Hello' ")
print(f"The variable 'b' has been assigned the integer value '20' i.e. 'b = 20' ")
print(f"The variable 'c' has been assigned the float value '20.5' i.e. 'c = 20.5' ")
print(f"The variable 'd' has been assigned the complex value '1j' i.e. 'd = 1j' ")
print(f"The variable 'e' has been assigned the a multi-line string value" + e + "\n")

print("\nVariable Types\n---------------------------------------------------------")
print(f"The value of variable 'a' is {a} and is of type:{type(a)}") #Using F strings
print(f"The value of variable 'b' is {b} and is of type:{type(b)}") #Using F strings (can handle integers)
print("The value of variable 'c' is " + str(c) + " and is of type:" + str(type(c))) #Using Concatenation (must convert int to string)

print("\nString Manipulation\n---------------------------------------------------------")
print(f"The number of characters in variable 'e' is {len(e)} (by using the len() method)")
print(f"Use the keyword 'in' (Boolean result) to search for a word/character withing a string, e.g. 'et' in 'e' returns {'et' in e}")
print(f"Use the upper() method to change casing e.g. a.upper() will return {a.upper()}")
print(f"Use the lower() method to change casing e.g. a.lower() will return {a.lower()}")
print(f"Python string slicing can return a range of characters e.g., 'print(a[1:4])' will return {print(a[1:4])}")
#print(a[:8]) will slice from the start
#print(a[1:]) will slice to the end
#print(a[-5:-2]) uses negative indexing


print("\nIn python strings are arrays; characters can be accessed via indexes or through looping.")
print(f"Print the second letter of variable 'a' ({a}): " + a[1]) #Will print 'e'
print(f"Print the fifth letter of variable 'a' ({a}): " + a[4]) #Will print 'o'
print("It is possible to loop through strings:")
for x in a:
	print(x)




print("\nType Casting\n---------------------------------------------------------")
print(f"Convert integer 'b' to float with the respective function - float(var_name); new value is: {float(b)} and type is {type(float(b))}")
