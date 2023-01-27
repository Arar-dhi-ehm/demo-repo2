
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # Create method within a class. __init__ is method
    def __init__(self, first, last, pay):  # self is an instance & arg; first,last,pay are arguments
        self.first = first  # Attribute of class
        self.last = last
        self.email = f'{first}.{last}@fpt.com'
        self.pay = pay

        Employee.num_of_emps += 1

    # Create method to get employee Full Name
    def full_name(self):
        return f'{self.first} {self.last}'

    # Create method for pay_raise
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # Take the class as the first argument instead of the instance 'self'
    @classmethod  # This decorator make the class as method
    def set_raise_amount(a_class, amount):
        a_class.raise_amount = amount  # Set class variable raise_amt to amount

# Instances of class Employee
employee_1 = Employee('Aaron', 'Patton', 50000)  # (Instance Attributes)
employee_2 = Employee('Joshua', 'Sims', 60000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
