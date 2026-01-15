# Object-Oriented Programming (OOP) in Python

"""
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.
It helps organize code into reusable and modular components.

Key concepts in OOP:
1. Class: A blueprint for creating objects.
2. Object: An instance of a class.
3. Encapsulation: Bundling data and methods that operate on that data within a class.
4. Inheritance: Creating new classes from existing ones.
5. Polymorphism: Ability of different classes to be treated as instances of the same class through inheritance.
6. Abstraction: Hiding complex implementation details and showing only essential features.

In Python, everything is an object, and OOP is fully supported.
"""

# Example 1: Basic Class and Object
class Car:
    """A simple Car class demonstrating basic OOP concepts."""

    def __init__(self, make, model, year):
        """Constructor method to initialize object attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        """Method to increase speed."""
        self.speed += increment
        print(f"{self.make} {self.model} is now going {self.speed} km/h")

    def brake(self, decrement):
        """Method to decrease speed."""
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
        print(f"{self.make} {self.model} slowed down to {self.speed} km/h")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Using object methods
car1.accelerate(50)
car2.accelerate(40)
car1.brake(20)

print(f"Car 1: {car1.make} {car1.model} ({car1.year})")
print(f"Car 2: {car2.make} {car2.model} ({car2.year})")

# Example 2: Inheritance
class ElectricCar(Car):
    """ElectricCar inherits from Car class."""

    def __init__(self, make, model, year, battery_capacity):
        """Initialize ElectricCar with additional battery attribute."""
        super().__init__(make, model, year)  # Call parent constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        """Method specific to ElectricCar."""
        print(f"{self.make} {self.model} is charging. Battery: {self.battery_capacity} kWh")

# Creating an ElectricCar object
electric_car = ElectricCar("Tesla", "Model 3", 2023, 75)
electric_car.accelerate(60)
electric_car.charge()

# Example 3: Polymorphism
def describe_vehicle(vehicle):
    """Function demonstrating polymorphism - works with any vehicle type."""
    print(f"This is a {vehicle.year} {vehicle.make} {vehicle.model}")

describe_vehicle(car1)
describe_vehicle(electric_car)

# Example 4: Encapsulation
class BankAccount:
    """BankAccount class demonstrating encapsulation."""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (encapsulated)

    def deposit(self, amount):
        """Method to deposit money."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """Method to withdraw money."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        """Method to check balance (controlled access to private attribute)."""
        return self.__balance

# Creating a bank account
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")


# Trying to access private attribute directly (not recommended)
# print(account.__balance)  # This would raise AttributeError
# Instead, use the public method
print(f"Balance via method: ${account.get_balance()}")

# Example 5: Class Attributes vs Object Attributes
class Dog:
    """Dog class demonstrating class attributes and object attributes."""

    # Class attribute - shared by all instances of the class
    species = "Canis familiaris"  # All dogs are of this species
    total_dogs = 0  # Counter for total number of dog instances

    def __init__(self, name, breed, age):
        """Constructor with object attributes."""
        # Object attributes - unique to each instance
        self.name = name
        self.breed = breed
        self.age = age

        # Increment class attribute when a new dog is created
        Dog.total_dogs += 1

    def bark(self):
        """Method to make the dog bark."""
        print(f"{self.name} says: Woof!")

    @classmethod  #another is @staticmethod
    def get_total_dogs(cls):
        """Class method to get total number of dogs."""
        return cls.total_dogs

# Creating Dog objects
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Bulldog", 5)
dog3 = Dog("Bella", "Poodle", 2)

# Accessing object attributes (unique to each dog)
print(f"{dog1.name} is a {dog1.age}-year-old {dog1.breed}")
print(f"{dog2.name} is a {dog2.age}-year-old {dog2.breed}")
print(f"{dog3.name} is a {dog3.age}-year-old {dog3.breed}")

# Accessing class attributes (shared by all dogs)
print(f"All dogs are of species: {Dog.species}")
print(f"All dogs are of species: {dog1.species}")  # Can also access via instance
print(f"All dogs are of species: {dog2.species}")  # Same value for all instances

# Modifying class attribute affects all instances
Dog.species = "Domestic Dog"
print(f"Updated species: {dog1.species}")  # Changed for all
print(f"Updated species: {dog2.species}")  # Changed for all

# Modifying object attribute only affects that instance
dog1.age = 4
print(f"{dog1.name}'s age: {dog1.age}")  # Only dog1's age changed
print(f"{dog2.name}'s age: {dog2.age}")  # dog2's age unchanged

# Using class method
print(f"Total number of dogs created: {Dog.get_total_dogs()}")

# Calling instance methods
dog1.bark()
dog2.bark()
dog3.bark()


