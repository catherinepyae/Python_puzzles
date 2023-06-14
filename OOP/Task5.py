# function defined in a class is called a method
# when calling the method, don't need to pass a parameter explicitly for self
# u.norm() is translated into vector.norm(u)
# __init__ method is called a initializer
# methods that start and end with two underscores are sometimes called the magic methods or dunder methods

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx, newy)


u = Vector(3, 4)
v = Vector(3, 6)

# output: u + v is a vector object at some memory address
# need to implement __str__ in order to print the vector nicely


print(u+v)
