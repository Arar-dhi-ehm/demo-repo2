# A Python program to demonstrate inheritance

class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Class Inheritance
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Aaron")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Richard")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
