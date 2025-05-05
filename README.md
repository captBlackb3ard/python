# Python
This project contains the essentials for developing and maintaining Python code and utility scripts for system administration and security.

## Python Basics
Python is a programming language that can be used for data science, machine learning, software development, web development (server-side), and system scripting (task automation and maintenance).
The most recent version of Python is Python 3, which will be used for this project.

## Python Comments
* To add single line comments to a Python script, use the `#` character symbol.
* TO add multi-line comments to a Bash script, use the following characters (and spacing).
```
\```
 Everything within these characters will be a comment and will not be executed.
\```

"""
Everything within these characters will be a comment and will not be executed.
"""
```

## Running Python Scripts


## Rules for Variable Names
* Variable names can only contain letters, digits, and underscores
* Variable name cannot start with a digit
* Variable names are case-sensitive (Var and var are different)
* Avoid using [Python keywords](https://www.geeksforgeeks.org/python-keywords/) (e.g., if, else, for) 
```
Valid Examples
************************************
x = 21
_y = "world"
ac_balance = 100.0

Invalid Examples
************************************
1x = "Name"   #Starts with a digit
class = 10    #class is a reserved keyword
dept-code = 2 #Contains a hypen
```

## Variable Scope

### Global Scope
- Variable defined outside any function are global and can be accessed inside functions using the 'global' keyword
```
var_a = "Global variable"

print(var_a)

def functi():
	global var_a
	var_a = "Modified globally"
	print(a)

functi()
print(var_a)

#Output
Global variable
Modified globally
Modified globally

```

### Local Scope
- Variables desfined inside a function or class are local to that function/class.
```
def funct():
	var_b = "Local variable"
	print (var_b)

funct() #Will print the value 'Local variable'
print(var_b) #Will generate an error since 'var_b' is accessible outside the function
```

## Object Reference
- Assume that variable a is assigned the value of 10 i.e. `a = 10`, Python creates an object for the value 10 and makes `a` reference it. 
- If we assign another variable `b` to the variable `a`, then `b` refences the same object as `x` i.e. 10 and not variable `a`. 
 - If we reference a new object to variable `a` e.g, `a = "Hello"`, Python creates a new object for the value "Hello" and makes `a` reference this new object
 - Python variables hold references to objects, not the actual objects themselves
 ```
 a = 10
 b = a
 print(a) #Outputs 10
 print(b) #Outputs 10
 a = "Hello"
 print(a) #Outputs 'Hello'
 print(b) #Outputs 10
 ```

 ## Delete Variable Using `del` Keyword
 - The `del` keyword removes a variable from the namespace & effectively deletes the variable & frees up the memory it was using.
 ```
 #Create variable and reference value
 a = 10
 print(a)

 del a #Remove the variable

 print(a) #Error generated after deleting variable a: name 'a' is not defined.
 ```