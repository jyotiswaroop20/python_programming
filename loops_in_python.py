#loops in Python
#define loops in Python - A loop is a programming construct that repeats a block of code as long as a specified condition is true.

#define two main types of loops in Python: for loops and while loops.
# For loop
for i in range(5):
    print(i) #output: 0 1 2 3 4

# While loop
count = 0
while count < 5:
    print(count)  #output: 0 1 2 3 4
    count += 1

# Loop control statements
# Break statement - used to exit a loop prematurely
for i in range(10):
    if i == 5:
        break
    print(i)  #output: 0 1 2 3 4

# Continue statement - used to skip the current iteration and move to the next one
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  #output: 1 3 5 7 9

# Nested loops - loops inside other loops
for i in range(3):
    for j in range(2):
        print(f'i: {i}, j: {j}')
#output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1

# Looping through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
#output:
# apple
# banana
# cherry

# Looping through a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
#output:
# name: Alice
# age: 25
# city: New York

# Using else with loops - the else block executes when the loop completes normally (not via break)
for i in range(3):
    print(i)
else:
    print("Loop completed")
#output:
# 0
# 1
# 2
# Loop completed

# List comprehension with loops
squares = [x**2 for x in range(5)]
print(squares)  #output: [0, 1, 4, 9, 16]

# While loop with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed")
#output:
# 0
# 1
# 2
# While loop completed

# Infinite loop (use with caution)
# Uncomment the following lines to see an infinite loop in action
# while True:
#     print("This will run forever unless stopped manually")
# Note: To stop an infinite loop, you can usually press Ctrl+C in the terminal or command prompt.
# Summary: Loops are essential for iterating over data structures and executing repetitive tasks efficiently in Python.

