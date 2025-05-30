#!/usr/bin/python3

#/**Python Object Oriented Programming: Classes**/
#/**----------------------------------------------------------------------

# Very Basic Class Definition
class MyClass:
    x = 10

# Use the '__init__()' function to assign values to object properties during class definition
# The '__init__()' function is called automatically everytime the class is being used to create a new object
# The 'self' parameter is a reference to the current class object instance (it can be any other name but must be the first parameter in the class methods - see MathClass below)  
class Pet:
    def __init__(self, name, color, pettype):
        self.name = name
        self.color = color
        self.pettype = pettype

    def name(self):
        print(f"{self.name} is the name of your pet.")

    def pet_details(self):
        print(f"{self.name} is a {self.pettype} and is {self.color} in color.")

    def sound(self):
        print(f"{self.name} makes a sound!")

# Use the '__str__()' function to control what should be returned when the class object is represented as a string
# If the '__str__()' function is not set, the string representation of the object is returned
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self): #If this is not provided, printing the class object will return the memory address
        return f"{self.name}({self.age},{self.gender})"
    

#/**Python Object Oriented Programming: Object Methods**/
#/**----------------------------------------------------------------------
class MathClass:
    def __init__(nums, x, y):
        nums.x = x
        nums.y = y
    
    def addition(nums):
        return nums.x + nums.y

    def subtraction(nums):
        if(nums.x > nums.y):
            print(f"Difference of {nums.x} - {nums.y} is equal to: {nums.x - nums.y}")
        elif(nums.y > nums.x):
            print(f"Difference of {nums.y} - {nums.x} is equal to: {nums.y - nums.x}")
        else:
            print("x is equal to y: Difference is 0")



#/**Python Object Oriented Programming: Inheritance**/
#/**----------------------------------------------------------------------
class Dog(Pet):
    def speak(self):
        print(f"{self.name} is a {self.color} dog, and dogs bark!")


class Cat(Pet):
    def __init__(self, name, color, pettype):
        super().__init__(name, color, pettype) #Ensures the child class inherits all the parent class methods & properties

    def speak(self):
        print(f"{self.name} is a {self.color} cat, and cats meow!")

    def pet_details(self):
        super().pet_details()


#/**Object Creation**/
#/**----------------------------------------------------------------------

obj1 = MyClass()
print("\nPython Object Oriented Programming: Class Definition\n---------------------------------------------------------")
print(f"The value of the MyClass property 'x' is {obj1.x}")

# Class with __init__() method defined
pet1 = Pet("Buddy", "brown", "dog")
print(f"You created an a pet object for a {pet1.pettype}.")
print(f"The name of the pet is {pet1.name}")
pet1.pet_details()

# Class with __str__() method defined
p1 = Person("thor", 45, "male")
print(f"\nIn my opinion, {p1.name.capitalize()} is an overrated {p1.age} year old {p1.gender} hero.")
print(p1)

#Modify object properties
p1.name = "Hawk Eye"
print(f"\nModify class object properties with the syntax object_name.property_name = 'new value', e.g, p1.name = 'Hawk Eye' will update the respective object")
print(p1)

#Delete object properties
del p1.gender #On its own will generate error
print(f"\nUse the 'del' keyword to delete an object property value, e.g., del p1.gender will remove the 'gender' class property value")
del p1 #Will completely delete the property.
print(f"\nUse the 'del' keyword to delete an object property, e.g., del p1 will completely delete the p1 object")

# Class with methods defined
math = MathClass(18, 18)
print(f"\nThe sum of 10 and 8 is: {math.addition()}")
math.subtraction()

print("\nPython Object Oriented Programming: Inheritance\n---------------------------------------------------------")
##Class Inheritance
buddy = Dog("Buddy", "white", "dog")
buddy.speak()

leo = Cat("Leo", "grey", "cat")
leo.speak() #Child only method
leo.pet_details() #Child-Parent inherited method