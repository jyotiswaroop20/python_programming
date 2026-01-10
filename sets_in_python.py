#sets in Python are unordered collections of unique elements. 
# They are defined using curly braces {} or the set() constructor.
# sets are mutable, meaning you can add or remove elements after creation.
# Duplicate elements are automatically removed in a set.
# sets values must be immutable types like numbers, strings, or tuples.
# Example of values must be immutable:
# Example: (1, 2, 3) is valid but [1, 2, 3] is not valid as list is mutable.
# Means you can add new element in sets but you cannot change existing element.


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding elements to a set
my_set.add(6)
print("After adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)  # Raises KeyError if 3 is not found
print("After removing 3:", my_set)

my_set.discard(4)  # Does not raise an error if 4 is not found
print("After discarding 4:", my_set)

# creating a null set
null_set = set()
print("Null Set:", null_set)

# Accepting user input to create a set
n = int(input("Enter number of elements you want to add to the set: "))
for _ in range(n):
    element = int(input("Enter element: "))
    null_set.add(element)
print("User Set:", null_set)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Union
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set) #output: {1, 2, 3, 4, 5, 6}
# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)  #output: {3, 4}
# Difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (set_a - set_b):", difference_set)
# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of set_a and set_b:", symmetric_difference_set)

#Duplicate elements in a list can be removed by converting the list to a set
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", my_list)
unique_set = set(my_list)
print("Set with unique elements:", unique_set)

# Converting the set back to a list
unique_list = list(unique_set)
print("List with unique elements:", unique_list)

#typeof set
print("Type of my_set:", type(my_set))  # Output: <class 'set>
print("Type of null_set:", type(null_set))  # Output: <class 'set'>
print("Type of unique_set:", type(unique_set))  # Output: <class 'set'>
print("Type of unique_list:", type(unique_list))  # Output: <class 'list'>

# len() function to get the number of elements in a set
print("Length of my_set:", len(my_set))  # Output: Length of my_set: 4
print("Length of null_set:", len(null_set))  # Output: Length of null_set: n
print("Length of unique_set:", len(unique_set))  # Output: Length of unique_set: 5
print("Length of unique_list:", len(unique_list))  # Output: Length of unique_list: 5

# Set methods
print("Is 2 in my_set?", 2 in my_set)  # Output: True
print("Is 10 in my_set?", 10 in my_set)  # Output: False
print("Set Elements:", my_set)  # Output: Set Elements: {1, 2, 5, 6}
my_set.clear()
print("After clear:", my_set)  # Output: After clear: set()

#add method
my_set.add(10)
print("After adding 10:", my_set)  # Output: After adding 10: {10}
my_set.add(20)
print("After adding 20:", my_set)  # Output: After adding 20: {10, 20}

#remove method
my_set.remove(10)
print("After removing 10:", my_set)  # Output: After removing 10: {20}

#pop method
popped_element = my_set.pop()
print("Popped Element:", popped_element)  # Output: Popped Element: 20
print("After popping element:", my_set)  # Output: After popping element: set()

