# Create a class
class myClass:
    x = 5


print(myClass)

# using class named 'myClass' to create objects

p1 = myClass()
print(p1.x)

# __init__() function
# all classes have a function called __init__()
# which is always executed when the class is being initiated
# __init__() function is use to assign values to object properties or other operations that are necessary to do when the object is being created
# __init__() function is automatically called every time the class is being used to create a new object


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("J", 27)
print(p1.name)
print(p1.age)

# __str__() function
# controls what should be returned when the class object is represented as a string
# it's not a set,

# without __str__() function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("cat", 27)

print(p1)

# with __str__() function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("cat", 27)

print(p1)
