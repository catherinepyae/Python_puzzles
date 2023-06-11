# Collections
# next five most important types in Python
# Strings
# lists
# typles
# dictionaries and
# sets

# Lists(list)

# Lists are ordered sequences of objects
# Objects do not have to be the same type
# they are indicated by square brackets and the elements of the list are separated by commas
# possible to index into a list as we did in string

L = [1, 2, 3, 4, 5]
print(type(L))
L.append(5)
print(L)
print("The first item is:", L[0])
print("The second item is: ", L[1])
print("The last item is", L[-1])
print("The second to last item is", L[-2])  # still got wrong ans

# Turples
# Tuples also ordered sequences of objects but unlike lists, they are immutable
# can access the items but can't change what items are in the tuple after created them
# trying to append raises an exception

t = (1, 2, "Hello")  # turple

print(type(t))
print(t)
print(t[2])
# t.append(101)#raises an exception
# t[2] = "hi"#raises an exception
# s='000000'
# s[4]='x'#raise exception
