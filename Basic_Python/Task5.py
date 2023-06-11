# Iterating over a collection
# very common to want to loop over a collection
# the pythonic way of doing iteration is with a for loop

myList = [1, 3, 5]
mytuple = (1, 2, "skip a few", 99, 100)
myset = {'a', 'b', 'c'}
mystring = "this is string"
mydict = {'a': "apple", 'b': "ball"}

for item in myList:
    print(item)

for item in mytuple:
    print(item)

for item in myset:
    print(item)

for item in mydict:
    print(item)

for character in mystring:
    print(character)
