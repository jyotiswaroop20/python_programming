#String functions in Python
#Python provides various built-in functions to manipulate and work with strings.
#Example of string functions in Python
my_string = "Hello, World!"
print("Original string:", my_string)

#Using the len() function to get the length of the string
string_length = len(my_string)
print("Length of the string:", string_length)

#Using the str() function to convert other data types to string
number = 100
number_string = str(number)
print("Converted number to string:", number_string)

#Using the ord() function to get the Unicode code point of a character
char = 'A'
char1 = 'a'
unicode_value = ord(char)
unicode_value1 = ord(char1)
print("Unicode value of", char1, "is:", unicode_value1)
print("Unicode value of", char, "is:", unicode_value)

#Using the chr() function to get the character from a Unicode code point
unicode_point = 66
character = chr(unicode_point)
print("Character for Unicode value", unicode_point, "is:", character)

#Using the format() method to format strings
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted string using format():", formatted_string)

#Using the f-string for formatting (available in Python 3.6 and later)
f_string = f"My name is {name} and I am {age} years old."
print("Formatted string using f-string:", f_string)

#Using the split() method to split a string into a list
sentence = "This is a sample string."
words = sentence.split(" ")
print("Split string into words:", words)

#Using the join() method to join a list of strings into a single string
joined_string = " ".join(words)
print("Joined string:", joined_string)

#Using the replace() method to replace a substring with another substring
new_string = my_string.replace("World", "Python")
print("String after replacement:", new_string)

#Using the upper() method to convert a string to uppercase
upper_string = my_string.upper()
print("Uppercase string:", upper_string)

#Using the lower() method to convert a string to lowercase
lower_string = my_string.lower()
print("Lowercase string:", lower_string)

#Using the strip() method to remove leading and trailing whitespace
whitespace_string = "   Hello, Python!   "
stripped_string = whitespace_string.strip()
print("Stripped string:", stripped_string)

#Using the find() method to find the index of a substring
index = my_string.find("World")
print("Index of 'World' in my_string:", index)

#Using the count() method to count occurrences of a substring
count = my_string.count("o")
print("Count of 'o' in my_string:", count)

#Using the startswith() method to check if a string starts with a specific substring
starts_with_hello = my_string.startswith("Hello")
print("Does my_string start with 'Hello'?", starts_with_hello)

#Using the endswith() method to check if a string ends with a specific substring
ends_with_exclamation = my_string.endswith("!")
print("Does my_string end with '!'?", ends_with_exclamation)

#Using the isalpha() method to check if all characters in the string are alphabetic
is_alpha = my_string.isalpha()
print("Is my_string alphabetic?", is_alpha)

#Using the isdigit() method to check if all characters in the string are digits
is_digit = "12345".isdigit()
print("Is '12345' numeric?", is_digit)

#Using the capitalize() method to capitalize the first character of the string
capitalized_string = my_string.capitalize()
print("Capitalized string:", capitalized_string)

#Using the title() method to capitalize the first character of each word in the string
title_string = my_string.title()
print("Title case string:", title_string)

#Using the zfill() method to pad a string with zeros on the left
padded_string = "42".zfill(5)
print("Padded string with zeros:", padded_string)

#End of string_function.py