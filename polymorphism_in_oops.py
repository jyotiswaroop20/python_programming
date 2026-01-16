# Polymorphism in Python OOP

"""
Polymorphism is the ability of different objects to respond to the same method call in different ways.
The term "polymorphism" means "many forms".

Types of polymorphism in Python:
1. Method Overriding: Child class provides specific implementation of a method from parent class
2. Operator Overloading: Giving special meaning to operators for user-defined classes
3. Duck Typing: Objects of different types can be used interchangeably if they have the right methods
"""

# Method Overriding Example
class Animal:
    """Base class for animals."""

    def speak(self):
        """Generic speak method."""
        return "Some animal sound"

class Dog(Animal):
    """Dog class overriding speak method."""

    def speak(self):
        return "Woof!"

class Cat(Animal):
    """Cat class overriding speak method."""

    def speak(self):
        return "Meow!"

# Function demonstrating polymorphism
def animal_sound(animal):
    """Function that works with any animal object."""
    return animal.speak()

# Creating objects
dog = Dog()
cat = Cat()
generic_animal = Animal()

print("Method Overriding (Polymorphism):")
print(f"Dog: {animal_sound(dog)}")
print(f"Cat: {animal_sound(cat)}")
print(f"Generic Animal: {animal_sound(generic_animal)}")

# Operator Overloading Example
class Vector:
    """Vector class demonstrating operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): #this id dunder function
        """Overload + operator."""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        """Overload str() function for printing."""
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        """Overload == operator."""
        return self.x == other.x and self.y == other.y

# Using operator overloading
v1 = Vector(2, 3)
v2 = Vector(1, 4)

print("\nOperator Overloading:")
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")  # Uses __add__
print(f"v1 == v2: {v1 == v2}")  # Uses __eq__

# Another operator overloading example
class ComplexNumber:
    """Complex number class with operator overloading."""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 4)

print(f"\nComplex Numbers:")
print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c1 + c2: {c1 + c2}")
print(f"c1 * c2: {c1 * c2}")

# Types of Dunder (Magic) Functions in Python
"""
Dunder functions (double underscore functions) are special methods in Python that start and end with __.
They are also called magic methods or special methods.

Main categories of dunder functions:

1. Object Creation & Destruction:
   - __new__(cls, ...)     : Object creation (rarely overridden)
   - __init__(self, ...)   : Object initialization
   - __del__(self)         : Object destruction (garbage collection)

2. String Representation:
   - __str__(self)         : String for end users (str())
   - __repr__(self)        : String for developers (repr())
   - __format__(self, format_spec) : Custom formatting

3. Arithmetic Operators:
   - __add__(self, other)      : Addition (+)
   - __sub__(self, other)      : Subtraction (-)
   - __mul__(self, other)      : Multiplication (*)
   - __truediv__(self, other)  : Division (/)
   - __floordiv__(self, other) : Floor division (//)
   - __mod__(self, other)      : Modulo (%)
   - __pow__(self, other)      : Power (**)

4. Comparison Operators:
   - __eq__(self, other)   : Equal (==)
   - __ne__(self, other)   : Not equal (!=)
   - __lt__(self, other)   : Less than (<)
   - __le__(self, other)   : Less or equal (<=)
   - __gt__(self, other)   : Greater than (>)
   - __ge__(self, other)   : Greater or equal (>=)

5. Assignment Operators (In-place):
   - __iadd__(self, other) : += 
   - __isub__(self, other) : -=
   - __imul__(self, other) : *=
   - etc.

6. Unary Operators:
   - __neg__(self)     : Negative (-x)
   - __pos__(self)     : Positive (+x)
   - __abs__(self)     : Absolute value (abs())
   - __invert__(self)  : Bitwise not (~)

7. Container/Sequence Methods:
   - __len__(self)          : Length (len())
   - __getitem__(self, key) : Indexing (obj[key])
   - __setitem__(self, key, value) : Assignment (obj[key] = value)
   - __delitem__(self, key) : Deletion (del obj[key])
   - __iter__(self)         : Iteration (for x in obj)
   - __next__(self)         : Next item (next())

8. Context Managers:
   - __enter__(self)    : Enter context (with statement)
   - __exit__(self, exc_type, exc_val, traceback) : Exit context

9. Callable Objects:
   - __call__(self, ...) : Make object callable (obj())

10. Attribute Access:
    - __getattr__(self, name)     : Get attribute
    - __setattr__(self, name, value) : Set attribute
    - __delattr__(self, name)     : Delete attribute
    - __getattribute__(self, name) : Get attribute (called first)

There are over 100 dunder methods in Python, but these are the most commonly used ones.
"""

# Example showing more dunder methods
class CustomList:
    """Custom list class demonstrating various dunder methods."""

    def __init__(self, items=None):
        self.items = items or []

    def __len__(self):
        """Return length of the list."""
        return len(self.items)

    def __getitem__(self, index):
        """Get item by index."""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set item by index."""
        self.items[index] = value

    def __str__(self):
        """String representation."""
        return f"CustomList({self.items})"

    def __add__(self, other):
        """Concatenate two CustomList objects."""
        return CustomList(self.items + other.items)

# Demonstrating various dunder methods
custom_list = CustomList([1, 2, 3])
print(f"\nCustom List: {custom_list}")
print(f"Length: {len(custom_list)}")  # __len__
print(f"Item at index 1: {custom_list[1]}")  # __getitem__

custom_list[0] = 10  # __setitem__
print(f"After modification: {custom_list}")

list2 = CustomList([4, 5])
combined = custom_list + list2  # __add__
print(f"Combined list: {combined}")