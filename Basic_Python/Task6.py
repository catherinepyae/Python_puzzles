# Other forms of control flow
# control flow affect the order in which operations are executed.
# example , for loop
# other basic form of control flow are
# if statements
# while loops
# try blocks
# function calls

# if statement
if 3+3 < 7:
    print("This should be printed.")

if 2 ** 8 != 256:
    print("This should not be printed.")

# if else statement
if False:
    print("This is bad")
else:
    print("This will print:")

# while loop
x = 1
while x < 128:
    print(x, end=" ")
    x = x*2

# try block
# it's a way to catch and recover from errors while a program is running
# if have some code that may cause an error, but don't want it to crash program, can put the code in a try block
# then can catch the error(also known as an exception)

x = "not a number"
try:
    f = float(x)
except ValueError:
    print("You can't do that!")

# function
# also change the control flow
# define a function with the def keyword
# This keyword creates an object to store the block of code
# parameters for the function are listed in parentheses after the function name
# return statement causes the control flow to revert back to where the function was called and determines the value of the function call


def foo(x, y):
    return 8*x+y


print(foo(2, 1))
print(foo("Na", "batman"))

# even if we define a function twice,
# even if we change the parameters, the first will be overwritten by the second


def foo(x):
    return (2+x)


def bar(somefunction):
    return (somefunction(4))


print(foo(2))
print(bar(foo))
