# Python Object_Oriented_Programming

# Classes and Instances
# Classes allow us to logically group our data and functions in a way that's easy to reuse
# also easy to build upon if need be
# method = functions that are associated with the class
# a class is a blueprint for creating instances

# first way with too many codes
class Employee:
    pass  # skip that for now


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = "Pyae"
emp_1.last = "Phyo"
emp_1.email = "Pyae.Phyo@gmail.com"
emp_1.payment = "10 lakh"

emp_2.first = "Kaung"
emp_2.last = "Myat"
emp_2.email = "Kaung.Myat@gmail.com"
emp_2.payment = "10 lakh"

print(emp_2.payment)
print('{} {}'.format(emp_1.first, emp_1.last))

# second way with less code


class Employee_update:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # each class within the class automatically takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


empupdate_1 = Employee_update("Pyae", "Phyo", "10 lakh")
empupdate_2 = Employee_update("Kaung", "Myat", "10 lakh")

print(empupdate_1.fullname())
print(empupdate_1.email)
print(empupdate_2.email)
