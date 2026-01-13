#function in python
#defination a function - function is a block of code which only runs when it is called.
#you can pass data, known as parameters, into a function.
#A function can return data as a result.
#syntax
#def function_name(parameters):
    #function body
    #return statement

#example
def greet(name):
    return "Hello, " + name + "!"
#calling the function
print(greet("Alice"))  # Output: Hello, Alice!

#example with multiple parameters
def add(a, b):
    return a + b
#calling the function
print(add(5, 3))  # Output: 8

#example with no parameters
def say_hello():
    return "Hello, World!"
#calling the function
print(say_hello())  # Output: Hello, World!

#example with default parameters
def greet_with_default(name="Guest"):
    return "Hello, " + name + "!"
#calling the function
print(greet_with_default())        # Output: Hello, Guest!
print(greet_with_default("Bob"))   # Output: Hello, Bob!

#example with keyword arguments
def describe_person(name, age):
    return f"{name} is {age} years old."
#calling the function
print(describe_person(age=30, name="Charlie"))  # Output: Charlie is 30 years old.

#example with variable-length arguments
def sum_all(*args):
    return sum(args)
#calling the function
print(sum_all(1, 2, 3, 4, 5))  # Output: 15

#example with lambda function
square = lambda x: x * x
#calling the lambda function
print(square(6))  # Output: 36

#example with nested functions
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()
#calling the outer function
print(outer_function("hello"))  # Output: HELLO

#example with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#calling the recursive function
print(factorial(5))  # Output: 120

#example with docstring
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b
#calling the function
print(multiply(4, 5))  # Output: 20
#accessing the docstring
print(multiply.__doc__)  # Output: Returns the product of a and b.

#example with type hints
def divide(a: float, b: float) -> float:
    return a / b
#calling the function
print(divide(10.0, 2.0))  # Output: 5.0

#example with function annotations
def greet_annotated(name: str) -> str:
    return "Hello, " + name + "!"
#calling the function
print(greet_annotated("Diana"))  # Output: Hello, Diana!


#built-in functions in python
#len() - returns the length of an object
print(len("Hello"))  # Output: 5

#type() - returns the type of an object
print(type(10))  # Output: <class 'int'>

#max() - returns the largest item in an iterable or the largest of two or more arguments
print(max(1, 5, 3))  # Output: 5

# print function in python
print("This is a print statement.")  # Output: This is a print statement.

#input function in python
#name = input("Enter your name: ")
#print("Hello, " + name + "!")  # Output: Hello, <name>!