#!/usr/bin/python3

"""
- Equals                     a == b
- Not Equals                 a != b
- Less Than                  a < b
- Less than or equal to      a <= b
- Greater than               a > b
- Greater than or equal to   a >= b
"""

a = 20
b = 200 
c = 22
d = 22

print(f"Variable 'a' is {a}")
print(f"Variable 'b' is {b}")
print(f"Variable 'c' is {c}")
print(f"Variable 'd' is {d}")

#Indentation is very important for Python code blocks
#Simple if condition
print("\n'if' condition testing")
if b > a:
    print("b is greater than a")

print("\n'elif' condition testing")
#elif condition testing - if previous condition was not true
if c > d:
    print("c is greater than d")
elif c == d:
    print("c is equal to d")

print("\n'else' condition testing")
#else catches anything that the preceding conditions did not catch
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

#Logical Operations - and, or, not
print("\n'and' operator condition testing")
if b > a and c > a:
    print("Both conditions are true - b > a and c > a")

print("\n'or' operator condition testing")
if a < b or a > c:
    print("Atleast condition is true - a < b or a > c")

print("\n'not' operator condition testing")
if not a > b:
    print("a is NOT greater than b")

#Nested if statements
print("\nTesting nested if conditions")
if a > 10:
    print("Above 10, ")
    if a < 19:
        print("and also above 19.")
    else:
        print("but not above 21.")

#Pass statement - used when 'if' condition is empty (not supported)
print("\n'Pass' statement testing")
if b > a:
    pass #Used to avoid getting an error
print("'pass' statement executed without error")