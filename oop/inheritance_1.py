class Animal:

    # Attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")

# Inherit from Animal


class Dog(Animal):

    # New method in subclass
    def display(self):
        # Access name attribute of superclass using self
        print("My name is ", self.name)


# Create an object of the subclass
labrador = Dog()

# Access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# Call subclass method
labrador.display()
