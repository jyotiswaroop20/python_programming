#tuple in Python
#definition: Tuples are ordered, immutable collections of items in Python.
#example of immutable nature of tuples

my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
# Accessing elements
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# Slicing
print("Sliced Tuple (2nd to 4th):", my_tuple[1:4])

# Iterating through the tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)

# Length of the tuple
print("Length of the Tuple:", len(my_tuple))

# Checking membership
print("Is 4 in the tuple?", 4 in my_tuple)

# Attempting to change an element (will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# Attempting to append an element (will raise an error)
try:
    my_tuple.append(6)
except AttributeError as e:
    print("Error:", e)

# Attempting to remove an element (will raise an error)
try:
    my_tuple.remove(3)
except AttributeError as e:
    print("Error:", e)

# Demonstrating that tuples can contain mutable objects
mutable_tuple = (1, 2, [3, 4], 5)
print("Original Mutable Tuple:", mutable_tuple)

# Modifying the mutable object inside the tuple
mutable_tuple[2].append(6)
print("After Modifying the Mutable Object inside the Tuple:", mutable_tuple)

# Creating a new tuple by concatenation
new_tuple = my_tuple + (6, 7, 8)
print("New Tuple after Concatenation:", new_tuple)

# Creating a new tuple by repetition
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)

# Nested tuples
nested_tuple = (1, (2, 3), (4, (5, 6)))
print("Nested Tuple:", nested_tuple)
print("Accessing element 6 from Nested Tuple:", nested_tuple[2][1][1])

# Converting a list to a tuple
list_to_convert = [10, 20, 30]
converted_tuple = tuple(list_to_convert)
print("Converted Tuple from List:", converted_tuple)

# Converting a tuple to a list
tuple_to_convert = (40, 50, 60)
converted_list = list(tuple_to_convert)
print("Converted List from Tuple:", converted_list)

# Finding the index of an element
index_of_3 = my_tuple.index(3)
print("Index of element 3 in Tuple:", index_of_3)

# Counting occurrences of an element
count_of_2 = my_tuple.count(2)
print("Count of element 2 in Tuple:", count_of_2)

# Demonstrating immutability by creating a new tuple with modified values
modified_tuple = (10,) + my_tuple[1:]
print("Modified Tuple (First Element Changed to 10):", modified_tuple)

# Tuple with a single element
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)

# Empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Tuple packing and unpacking
packed_tuple = 1, 2, 3
print("Packed Tuple:", packed_tuple)
x, y, z = packed_tuple
print("Unpacked Values from Packed Tuple:", x, y, z)

# Demonstrating that tuples can be used as keys in dictionaries
tuple_key_dict = {(1, 2): "a", (3, 4): "b"}
print("Dictionary with Tuple Keys:", tuple_key_dict)

# Accessing value using tuple key
value = tuple_key_dict[(1, 2)]
print("Value for key (1, 2):", value)

#user input to create a tuple
user_input = input("Enter elements for the tuple separated by commas: ")
user_tuple = tuple(user_input.split(","))
print("User Created Tuple:", user_tuple)
occurrences_of_2 = user_tuple.count(2)
print("Count of element 2 in List:", occurrences_of_2)

#tuple index
index_of_4 = user_tuple.index('4')  # Note: input elements are strings
print("Index of element '4' in User Tuple:", index_of_4)

#tuple count occurrences of a value
count_of_value = user_tuple.count('value_to_check')  # replace 'value_to_check with actual value
print("Count of 'value_to_check' in User Tuple:", count_of_value)


