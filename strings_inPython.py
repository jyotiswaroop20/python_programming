#Strings in Python
#Strings are sequences of characters enclosed in single quotes, double quotes, or triple quotes.
#Example of a string in Python
my_string = "Hello, World!"
print(my_string)
#Strings can be accessed using indexing and slicing
first_character = my_string[0]
print("First character:", first_character)
substring = my_string[0:5]
print("Substring:", substring)
#Strings are immutable, meaning they cannot be changed after creation
#However, you can create a new string based on modifications of the original
new_string = my_string.replace("World", "Python")
print("Modified string:", new_string)
#Strings support various methods for manipulation
upper_string = my_string.upper()
print("Uppercase string:", upper_string)
lower_string = my_string.lower()
print("Lowercase string:", lower_string)
#You can concatenate strings using the + operator
greeting = "Hello" + ", " + "Python!"
print("Concatenated string:", greeting)
#You can also repeat strings using the * operator
repeated_string = "Ha" * 3
print("Repeated string:", repeated_string)
#Strings can be formatted using f-strings (available in Python 3.6 and later)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)
#You can check for substrings using the 'in' keyword
is_present = "World" in my_string
print("Is 'World' in my_string?", is_present)
#You can find the length of a string using the len() function
string_length = len(my_string)
print("Length of my_string:", string_length)
#Strings can be split into a list of substrings using the split() method
words = my_string.split(", ")
print("Split string into words:", words)
#You can join a list of strings into a single string using the join() method
joined_string = " ".join(words)
print("Joined string:", joined_string)
#Triple quotes can be used for multi-line strings
multi_line_string = """This is a multi-line
string in Python."""
print("Multi-line string:", multi_line_string)
#Escape sequences can be used to include special characters in strings
escaped_string = "He said, \"Hello!\"\nWelcome to Python."
print("Escaped string:", escaped_string)
#Raw strings can be created by prefixing the string with 'r' to ignore escape sequences
raw_string = r"C:\Users\Name\Documents"
print("Raw string:", raw_string)
#End of strings_inPython.py