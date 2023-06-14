# OOP
# primary goal of oop is to make it possible to write code that is close to the way you think
# a class is also a type
# in python, class and type are same
# object is an instance of a class

# python has list class
# if i create 'myList' list, then 'myList' is an objectof type class
myList = []
print(type(myList))
print(isinstance(myList, list))
print(isinstance(myList, str))


def mygenerator(n):
    for i in range(n):
        yield (i)


print(type(mygenerator))
print(mygenerator(5))
