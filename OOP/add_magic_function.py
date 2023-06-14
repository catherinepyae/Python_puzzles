# __add__() function is one of the magic method in Python
# it returns a new object, the addition of the other two objects
# it implements the addition operator "+" in Python

# Syntax: obj1.__add__(self,obj2) Syntax
# obj1:First object to add in the second object
# obj2:Second object to add in the first object

class GFG:
    def __init__(self, val):
        self.val = val

    def __add__(self, val2):
        return GFG(self.val + val2.val)

    def __str__(self):
        return f"{self.x,self.y}"


obj1 = GFG("Greeks")
obj2 = GFG("ForGreeks")
obj3 = obj1+obj2
print(obj3.val)
