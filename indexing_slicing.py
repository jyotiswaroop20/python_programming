#indexing and slicing in Python
#Indexing allows you to access individual elements of a sequence using their position
#Slicing allows you to access a range of elements in a sequence
#Example of indexing and slicing with a list
my_list = [10, 20, 30, 40, 50]
#Accessing elements using indexing
first_element = my_list[0]
print("First element:", first_element)
last_element = my_list[-1]
print("Last element:", last_element)
#Accessing a range of elements using slicing
sub_list = my_list[1:4]
print("Sub-list from index 1 to 3:", sub_list)
#Slicing with a step
step_slice = my_list[0:5:2]
print("Slice with step of 2:", step_slice)
#Example of indexing and slicing with a string
my_string = "Hello, World!"
#Accessing characters using indexing
first_character = my_string[0]
print("First character:", first_character)
last_character = my_string[-1]
print("Last character:", last_character)
#Accessing a substring using slicing
substring = my_string[7:12]
print("Substring from index 7 to 11:", substring)
#Slicing with a step
step_substring = my_string[0:13:2]
print("Substring with step of 2:", step_substring)
#Negative indexing and slicing
negative_index = my_string[-5]
print("Character at negative index -5:", negative_index)
negative_slice = my_string[-6:-1]
print("Substring from negative index -6 to -2:", negative_slice)
#End of indexing_slicing.py