# Inheritance in Python OOP

"""
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) where a child class
inherits properties and methods from a parent class. This promotes code reusability and
establishes a relationship between classes.

Key points:
- Child class inherits all public and protected members from parent class
- Child class can override inherited methods
- Child class can add new methods and attributes
- Use 'super()' to call parent class methods
"""

# Parent class
class Animal:
    """Base class representing an animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        """Method that can be overridden by child classes."""
        return "Some generic animal sound"

    def eat(self):
        """Common method for all animals."""
        return f"{self.name} is eating"

    def info(self):
        """Display animal information."""
        return f"{self.name} is a {self.species}"

# Child class inheriting from Animal
class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        """Override the parent method."""
        return "Woof! Woof!"

    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} is fetching the ball"

# Another child class
class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        """Override the parent method."""
        return "Meow!"

    def scratch(self):
        """Cat-specific method."""
        return f"{self.name} is scratching"

# Creating objects and demonstrating inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

print("Dog Information:")
print(dog.info())
print(dog.make_sound())
print(dog.eat())
print(dog.fetch())

print("\nCat Information:")
print(cat.info())
print(cat.make_sound())
print(cat.eat())
print(cat.scratch())

# Both inherit the common 'eat' method from Animal
print(f"\nBoth animals eat: {dog.eat()}, {cat.eat()}")



# Multilevel Inheritance Example
"""
Multilevel inheritance is when a class inherits from another class, 
which itself inherits from another class, creating a chain of inheritance.

Example: Grandparent -> Parent -> Child
"""

class Vehicle:
    """Base class for vehicles."""

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    """Car class inheriting from Vehicle."""

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving"

class ElectricCar(Car):
    """Electric car inheriting from Car (which inherits from Vehicle)."""

    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.brand} {self.model} is charging ({self.battery_capacity}kWh battery)"

# Demonstrating multilevel inheritance
tesla = ElectricCar("Tesla", "Model S", 100)

print("\nMultilevel Inheritance Example:")
print(tesla.start())    # Inherited from Vehicle
print(tesla.drive())    # Inherited from Car
print(tesla.charge())   # Own method


# Multiple Inheritance Example
"""
Multiple inheritance is when a class inherits from more than one parent class.
The child class inherits attributes and methods from all parent classes.

Syntax: class Child(Parent1, Parent2, ...):
"""

class Flyable:
    """Mixin class for flying capability."""

    def fly(self):
        return "Flying high in the sky"

class Swimmable:
    """Mixin class for swimming capability."""

    def swim(self):
        return "Swimming in the water"

class Duck(Flyable, Swimmable):
    """Duck class inheriting from both Flyable and Swimmable."""

    def __init__(self, name):
        self.name = name

    def quack(self):
        return f"{self.name} says Quack!"

# Demonstrating multiple inheritance
duck = Duck("Donald")

print("\nMultiple Inheritance Example:")
print(duck.quack())     # Own method
print(duck.fly())       # Inherited from Flyable
print(duck.swim())      # Inherited from Swimmable


