# Property decorator in Python OOP

"""
The @property decorator allows you to define methods that can be accessed like attributes.
It provides a way to implement getters, setters, and deleters for class attributes.

Benefits:
- Encapsulate attribute access
- Add validation or computation to attribute access
- Maintain backward compatibility when changing internal implementation
"""

class Circle:
    """Circle class demonstrating property decorator."""

    def __init__(self, radius):
        self._radius = radius  # Private attribute with underscore

    @property
    def radius(self):
        """Getter for radius - accessed like an attribute."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Property that computes area - read-only."""
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        """Property that computes circumference - read-only."""
        return 2 * 3.14159 * self._radius

# Creating and using the Circle class
circle = Circle(5)

print("Initial circle:")
print(f"Radius: {circle.radius}")  # Using property getter
print(f"Area: {circle.area}")      # Using computed property
print(f"Circumference: {circle.circumference}")

print("\nChanging radius using setter:")
circle.radius = 10  # Using property setter
print(f"New radius: {circle.radius}")
print(f"New area: {circle.area}")
print(f"New circumference: {circle.circumference}")

print("\nTrying invalid radius:")
try:
    circle.radius = -5  # This will raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Properties can also be used with @deleter, but that's less common
# @radius.deleter
# def radius(self):
# del self._radius

# Another example: Student marks and percentage
class Student:
    """Student class with marks and automatic percentage calculation."""

    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # Private attribute

    @property
    def marks(self):
        """Getter for marks."""
        return self._marks

    @marks.setter
    def marks(self, value):
        """Setter for marks with validation."""
        if not (0 <= value <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self._marks = value

    @property
    def percentage(self):
        """Computed property for percentage - automatically updates when marks change."""
        return f"{self._marks}%"

# Creating student and demonstrating property
student = Student("Rahul", 85)

print("\nStudent Marks Example:")
print(f"Student: {student.name}")
print(f"Marks: {student.marks}")
print(f"Percentage: {student.percentage}")

print("\nChanging marks:")
student.marks = 92  # Marks change
print(f"New marks: {student.marks}")
print(f"New percentage: {student.percentage}")  # Percentage automatically updates

print("\nTrying invalid marks:")
try:
    student.marks = 150  # Invalid marks
except ValueError as e:
    print(f"Error: {e}")


# Getter Decorator Explanation
"""
In Python, there is no separate @getter decorator. 
The @property decorator serves as the getter.

@property decorator:
- Allows a method to be accessed like an attribute
- Used to implement getters in Python
- Can be read-only or have corresponding setters

Syntax:
@property
def attribute_name(self):
    return self._attribute

This method can then be accessed as: object.attribute_name
"""

class Temperature:
    """Class demonstrating getter decorator usage."""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius temperature."""
        print("Getting celsius value...")
        return self._celsius

    @property
    def fahrenheit(self):
        """Getter for fahrenheit (computed property)."""
        return (self._celsius * 9/5) + 32

# Using getter
temp = Temperature(25)

print("\nGetter Decorator Example:")
print(f"Temperature in Celsius: {temp.celsius}")    # Calls getter
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")  # Calls computed getter
