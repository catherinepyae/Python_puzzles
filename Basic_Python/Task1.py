# Sequence : performing operations one at a time in a specified order
# Selection : Using conditional statements such as if to select which operations to execute
# Iteration : Repeating some operations using loops or recursion

# Variables, Types and state
# variables are just names/name of the object
# Every name is associated with some piece of data, called an object
# the name is a string of characters and it is mapped to an object
# every object has a type
# Atomic types in Python are integers, floats and booleans
# use type() function to check the type of the variable
x = 5
y = 3.2
z = True
print("x has type", type(x))
print("y has type", type(y))
print("z has type", type(z))

# think of an object as having three things:an identity, a type, and a value
# it's identity cannot change

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x == z)

# In python, cannot change the type of an object
# can reassign a variable to point to different object of a different type
# there are several functions that may seem to be changing the types of objects but they are really just creating a new object from the old

x = 2
print("x = ", x)
print("float(x) =", float(x))
print("x still has type", type(x))

print("Overwriting x.")
x = float(x)
print("Now, x has type", type(x))

# can do more elaborate things as well

numstring = "3.1415926"
y = float(numstring)
print("y has type", type(y))

best_number = 73
x = str(best_number)
print("x has type", type(x))

thisworks = float("inf")
print("float(\'inf\') has type", type(thisworks))
infinity_plue_one = float('inf') + 1
print(infinity_plue_one)
# last example introduced a new type, that of a string. A string is
# a sequence of characters. In Python, there is no special class for a single
# character (as in C for example). If you want a single character, you use a
# string of length one.
# The value of an object may or may not be changed, depending on the
# type of object. If the value can be changed, we say that the object is
# mutable. If it cannot be changed, we say that the object is immutable.
# For example, strings are immutable. If you want to change a string, for
# example, by converting it to lowercase, then you will be creating a new
