# Class methods in Python OOP

"""
Class methods are methods that are bound to the class rather than to an instance of the class.
They are defined using the @classmethod decorator and take 'cls' as their first parameter.

Key points:
- Can be called on the class itself or on instances
- Used for factory methods, class-level operations
- Cannot access instance attributes directly
- Can modify class state
"""

class Student:
    """Student class demonstrating class methods."""

    # Class variable to track total students
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1  # Increment class variable

    @classmethod
    def create_student(cls, name, grade):
        """Class method factory to create student instances."""
        print(f"Creating student: {name}")
        return cls(name, grade)

    @classmethod
    def get_total_students(cls):
        """Class method to get total number of students."""
        return f"Total students created: {cls.total_students}"

    @classmethod
    def from_string(cls, student_string):
        """Class method to create student from string (factory method)."""
        name, grade = student_string.split(',')
        return cls(name.strip(), grade.strip())

    def info(self):
        """Instance method to display student info."""
        return f"Student: {self.name}, Grade: {self.grade}"

# Using class methods
print("Creating students using class method:")
student1 = Student.create_student("Alice", "A")
student2 = Student.create_student("Bob", "B")

print("\nStudent info:")
print(student1.info())
print(student2.info())

print("\nUsing class method to get total:")
print(Student.get_total_students())

print("\nCreating student from string using class method:")
student3 = Student.from_string("Charlie, A+")
print(student3.info())

print("\nFinal total:")
print(Student.get_total_students())