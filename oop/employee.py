
class Employee:

    # Create method within a class. __init__ is method
    def __init__(self, first, last, pay):  # self is an instance & arg; first,last,pay are arguments
        self.first = first  # Attribute of class
        self.last = last
        self.email = f'{first}.{last}@fpt.com'
        self.pay = pay

    # Create method to get employee Full Name
    def full_name(self):
        return f'{self.first} {self.last}'


# Instances of class Employee
employee_1 = Employee('Aaron', 'Patton', 50000)  # (Instance Attributes)
employee_2 = Employee('Joshua', 'Sims', 60000)

print(employee_1.full_name())  # The full_name needs () because it is a method
print(employee_1.email)
print(Employee.full_name(employee_2))
print(employee_2.email)
