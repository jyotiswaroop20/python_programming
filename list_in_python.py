#Definition and operations on a list in Python
#lists are ordered, mutable collections of items in Python.

#list in python
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Accessing elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Slicing
print("Sliced List (2nd to 4th):", my_list[1:4])

# Appending an element
my_list.append(6)
print("After Appending 6:", my_list)

# Removing an element
my_list.remove(3)
print("After Removing 3:", my_list)

# Iterating through the list
print("Iterating through the list:")
for item in my_list:
    print(item)

# Length of the list
print("Length of the List:", len(my_list))

# Checking membership
print("Is 4 in the list?", 4 in my_list)

# Sorting the list
my_list.sort(reverse=True)
print("Sorted List in Descending Order:", my_list)

#sorting the list in ascending order
my_list.sort()
print("Sorted List in Ascending Order:", my_list)

# Extending the list
my_list.extend([7, 8, 9])
print("After Extending the List:", my_list)

#change an element
my_list[0] = 10
print("After Changing First Element to 10:", my_list)

#reversing the list
my_list.reverse()
print("After Reversing the List:", my_list)

#inserting an element at a specific position
my_list.insert(2, 15)
print("After Inserting 15 at index 2:", my_list)

#removing an element by index
removed_element = my_list.pop(3)
print("After Popping Element at index 3 (Removed {}):".format(removed_element), my_list)

#remove first occurrence of a value
my_list.remove(15)
print("After Removing First Occurrence of 15:", my_list)

#count occurrences of a value
count_of_4 = my_list.count(4)
print("Count of 4 in the List:", count_of_4)

#copying the list
copied_list = my_list.copy()
print("Copied List:", copied_list)

# Clearing the list
my_list.clear()
print("After Clearing the List:", my_list)



