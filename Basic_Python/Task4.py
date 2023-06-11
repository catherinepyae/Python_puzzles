# Some common things to do with collections
# there are several operations that can be performed on any of the collections classes
a = "a string"
b = ["my", "second", "favourite", "list"]
c = {1, "tuple"}
d = {'a': 'b', 'b': '2', 'c': 'False'}
e = {1, 1, 1, 1, 1, 1, 1}

print(len(a), len(b), len(c), len(d), len(e))

# For sequential types(list, turples, strings),
# can slice a sub-sequence of indices using square brackets and a colon
# Note:slicing a sequence creates a new object, means a big slice will do a lot of coping

a = "a string"
b = ["my", "second", "favourite", "list"]
c = (1, 2, 3, "tuple")

print(a[3:7])
print(a[1:-2])
print(b[1:])
print(c[:2])
