#Dictionary in Python is a built-in data type that allows you to store key-value pairs. 
# It is mutable, meaning you can change its content after creation. 
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "Marks": [85, 90, 88],
    "Subjects": ("Math", "Science", "English"),
}
# Accessing values using keys
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict.get("age"))  # Output: 30
print("City:", my_dict["city"])  # Output: New York
print("Subjects:", my_dict["Subjects"])  # Output: ('Math', 'Science', 'English')
print("Marks:", my_dict["Marks"])  # Output: [85, 90, 88]

# Modifying values
my_dict["age"] = 31  # Update age
my_dict["city"] = "Los Angeles"  # Update city
print("Updated Age:", my_dict["age"])  # Output: 31
print("Updated City:", my_dict["city"])  # Output: Los Angeles

# Adding new key-value pairs
my_dict["profession"] = "Engineer"
print("Added Profession:", my_dict["profession"])  # Output: Engineer

# Removing key-value pairs
del my_dict["Marks"]  # Remove Marks
print("After Deleting Marks:", my_dict)

removed_value = my_dict.pop("city")  # Remove city and get its value
print("Removed City:", removed_value)  # Output: Los Angeles
print("After Popping City:", my_dict)

#creating null dictionary and accepting user input
user_dict = {}
n = int(input("Enter number of key-value pairs you want to add: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value
print("User Dictionary:", user_dict)

#creating nested dictionary
nested_dict = {
    "person1": {
        "name": "Bob",
        "age": 25
    },
    "person2": {
        "name": "Carol",
        "age": 28
    }
}
print("Nested Dictionary:", nested_dict)

# Accessing nested dictionary values
print("Person1 Name:", nested_dict["person1"]["name"])  # Output: Bob
print("Person2 Age:", nested_dict["person2"]["age"])  # Output: 28

# Modifying nested dictionary values
nested_dict["person1"]["age"] = 26
print("Updated Person1 Age:", nested_dict["person1"]["age"])  # Output: 26

# Dictionary methods
print("Keys:", my_dict.keys())  # Output: dict_keys(['name', 'age', 'profession'])
print(list(my_dict.keys()))  # Output: ['name', 'age', 'profession']

print("Values:", my_dict.values())  # Output: dict_values(['Alice', 31, 'Engineer'])

print("Items:", my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('profession', 'Engineer')
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 31), ('profession', 'Engineer')]

print("Length of my_dict:", len(my_dict))  # Output: 3

print("Is 'name' in my_dict?", "name" in my_dict)  # Output: True
print("Is 'city' in my_dict?", "city" in my_dict)  # Output: False

#getting value using get method
print("Getting 'profession' using get():", my_dict.get("profession"))  # Output : Engineer
print("Getting 'city' using get():", my_dict.get("city"))  # Output : None

# update method
my_dict.update({"hobby": "painting", "age": 32})
print("After update:", my_dict)  # Output: {'name': 'Alice', 'age': 32, 'profession': 'Engineer', 'hobby': 'painting'}
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 32), ('profession', 'Engineer'), ('hobby', 'painting')]

# clear method
my_dict.clear()
print("After clear:", my_dict)  # Output: {}

# Diffrerence between print(my_dict["key"]) and print(my_dict.get("key"))
# Using my_dict["key"] will raise a KeyError if the key does not exist in the dictionary.
# Using my_dict.get("key") will return None (or a specified default value) if the key does not exist, avoiding an error.
print("Using my_dict.get('nonexistent_key'):", my_dict.get("nonexistent_key"))  # Output: None
# print("Using my_dict['nonexistent_key']:", my_dict["nonexistent_key"])  # This will raise a KeyError
# if i will use my_dict["nonexistent_key"] it will give error because the key is not present in the dictionary and
# after all code execution will stop but if i will use my_dict.get("nonexistent_key") it will not give error and
# will return None and rest of the code will execute properly.
#if we are using dupilicate keys in dictionary then previsous key will be overwritten by latest key.
dup_dict = {
    "key1": "value1",
    "key2": "value2",
    "key1": "new_value1"  # Duplicate key
}
print("Dictionary with duplicate keys:", dup_dict)  # Output: {'key1': 'new_value1', 'key2': 'value2'}
# In the above example, the value of "key1" is "new_value1" because the previous value "value1" was overwritten.

# Looping through a dictionary
sample_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
for key, value in sample_dict.items():
    print(f"Key: {key}, Value: {value}")

# Output:
# Key: a, Value: 1
# Key: b, Value: 2
# Key: c, Value: 3

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging two dictionaries
dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}
merged_dict = {**dict1, **dict2}  # dict2 values will overwrite dict1 values for duplicate keys
print("Merged Dictionary:", merged_dict)  # Output: {'x': 10, 'y': 30, 'z': 40}

# Copying a dictionary
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
print("Copied Dictionary:", copied_dict)  # Output: {'a': 1, 'b': 2}

# Checking if a key exists
key_to_check = "a"
if key_to_check in original_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
# Output: Key 'a' exists in the dictionary.
print(f"Key 'c' exists in the dictionary: {'c' in original_dict}")  # Output: False

# Using setdefault() method
setdefault_dict = {"name": "Alice"}
age = setdefault_dict.setdefault("age", 25)  # Adds 'age' key with value 25
print("After setdefault:", setdefault_dict)  # Output: {'name': 'Alice', 'age': 25}
print("Returned age:", age)  # Output: 25
# If the key already exists, setdefault() returns its value without changing the dictionary
name = setdefault_dict.setdefault("name", "Bob")
print("After setdefault for existing key:", setdefault_dict)  # Output: {'name': 'Alice', 'age': 25}
print("Returned name:", name)  # Output: Alice

# Using fromkeys() method
keys = ["a", "b", "c"]
default_value = 0
fromkeys_dict = dict.fromkeys(keys, default_value)
print("Dictionary from fromkeys():", fromkeys_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# If no default value is provided, None is used
fromkeys_dict_none = dict.fromkeys(keys)
print("Dictionary from fromkeys() with None:", fromkeys_dict_none)  # Output: {'a': None, 'b': None, 'c': None}

# Using the popitem() method
popitem_dict = {"x": 1, "y": 2, "z": 3}
key, value = popitem_dict.popitem()  # Removes and returns the last inserted key-value pair
print("Popped item:", (key, value))  # Output: Popped item: ('z', 3)
print("After popitem:", popitem_dict)  # Output: After popitem: {'x': 1, 'y': 2}
# Note: In Python versions before 3.7, popitem() removes an arbitrary item.

# Using the dict() constructor
constructed_dict = dict(name="David", age=40, city="Chicago")
print("Constructed Dictionary:", constructed_dict)  # Output: {'name': 'David', 'age': 40, 'city': 'Chicago'}

# Using the enumerate() function with dictionaries
enum_dict = {"a": 10, "b": 20, "c": 30}
for index, (key, value) in enumerate(enum_dict.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")
# Output:
# Index: 0, Key: a, Value: 10
# Index: 1, Key: b, Value: 20
# Index: 2, Key: c, Value: 30

# Using the zip() function to create a dictionary
keys = ["name", "age", "city"]
values = ["Eve", 29, "Miami"]
zipped_dict = dict(zip(keys, values))
print("Zipped Dictionary:", zipped_dict)  # Output: {'name': 'Eve', 'age': 29, 'city': 'Miami'}

# Using the filter() function with dictionaries
filter_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = dict(filter(lambda item: item[1] % 2 == 0, filter_dict.items()))
print("Filtered Dictionary (even values):", filtered_dict)  # Output: {'b': 2, 'd': 4}




