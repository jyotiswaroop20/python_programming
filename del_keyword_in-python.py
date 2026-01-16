# del keyword in Python OOP

"""
The 'del' keyword in Python is used to delete references to objects.
In Object-Oriented Programming (OOP), 'del' can be used to:

1. Delete instance attributes from objects
2. Delete entire objects, triggering the __del__ method for cleanup
3. Remove references to prevent memory leaks

The __del__ method is a destructor that gets called when an object is about to be destroyed.
It's useful for cleanup operations like closing files or network connections.
"""

# Example class demonstrating del keyword in OOP
class ResourceManager:
    """A class that manages a resource and demonstrates cleanup with del."""

    def __init__(self, name):
        """Initialize the resource manager with a name."""
        self.name = name
        self.resource = f"Resource for {name}"
        print(f"ResourceManager '{self.name}' created with {self.resource}")

    def use_resource(self):
        """Method to simulate using the resource."""
        if hasattr(self, 'resource'):
            print(f"Using {self.resource}")
        else:
            print(f"Resource for '{self.name}' is no longer available")

    def __del__(self):
        """Destructor method called when object is deleted."""
        print(f"Cleaning up ResourceManager '{self.name}'")
        # In a real scenario, you might close files, release locks, etc.

# Creating an object
manager = ResourceManager("Database Connection")

# Using the object
manager.use_resource()

# Deleting an attribute
print("\nDeleting the 'resource' attribute:")
del manager.resource
manager.use_resource()  # This will show the attribute is gone

# Deleting the entire object
print("\nDeleting the object:")
del manager
print("Object deleted. The __del__ method was called during garbage collection.")

# Note: The __del__ method may not be called immediately after del
# It depends on Python's garbage collection timing

# Simple short example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 25)
print(f"Name: {p.name}, Age: {p.age}")

# Delete attribute
del p.age
print(f"Name: {p.name}")  # age attribute is gone

# Delete object
del p
print("Person object deleted") 

