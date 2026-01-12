#practice questions for loops in python
# print numbers from 1 to 50 using for loop
for num in range(1, 51):
    print(num, end=' ')  #output: 1 2 3 ... 50
print()  # for newline

# print even numbers from 1 to 50 using for loop
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')  #output: 2 4 6 ... 50
print()  # for newline

# print odd numbers from 1 to 50 using for loop
for num in range(1, 51):
    if num % 2 != 0:
        print(num, end=' ')  #output: 1 3 5 ... 49
print()  # for newline

# calculate the sum of numbers from 1 to 50 using for loop
total_sum = 0
for num in range(1, 51):
    total_sum += num
print(total_sum)  #output: 1275

# find the factorial of a number using for loop
number = 6
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(factorial)  #output: 720

# print the multiplication table of a number using for loop
number = 8
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
#output:
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80

# print digits of a number in reverse order using for loop
number = 67890
for digit in str(number)[::-1]:
    print(digit, end=' ')  #output: 0 9 8 7 6
print()  # for newline

# check if a number is prime using for loop
num = 29
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num} is a prime number')  #output: 29 is a prime number
else:
    print(f'{num} is not a prime number')

# print Fibonacci series up to n terms using for loop
n_terms = 10
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=' ')  #output: 0 1 1 2 3 5 8 13 21 34
    a, b = b, a + b
print()  # for newline

# find the largest number in a list using for loop
numbers = [34, 67, 23, 89, 12, 90, 45]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)  #output: 90

# find the smallest number in a list using for loop
numbers = [34, 67, 23, 89, 12, 90, 45]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)  #output: 12

# calculate the average of numbers in a list using for loop
numbers = [34, 67, 23, 89, 12, 90, 45]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)  #output: 50.0

# count the number of vowels in a string using for loop
string = "Hello World, Welcome to Python Programming"
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print(count)  #output: 13

# search for an element in a list using for loop
elements = [10, 23, 45, 70, 11, 15, 90]
target = 15
found = False
for element in elements:
    if element == target:
        found = True
        break
if found:
    print(f'{target} found in the list')  #output: 15 found in the list
else:
    print(f'{target} not found in the list')

# print a pattern using nested for loops
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end=' ')
    print()
#output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

# print multiplication table from 1 to 10 using nested for loops
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:4}', end=' ')
    print()
#output:
#    1    2    3    4    5    6    7    8    9   10 
#    2    4    6    8   10   12   14   16   18   20 
#    3    6    9   12   15   18   21   24   27   30 
#    4    8   12   16   20   24   28   32   36   40 
#    5   10   15   20   25   30   35   40   45   50 
#    6   12   18   24   30   36   42   48   54   60 
#    7   14   21   28   35   42   49   56   63   70 
#    8   16   24   32   40   48   56   64   72   80 
#    9   18   27   36   45   54   63   72   81   90 
#   10   20   30   40   50   60   70   80   90  100

# print characters of a string in reverse order using for loop
string = "Python"
for char in string[::-1]:
    print(char, end=' ')  #output: n o h t y P
print()  # for newline

#range function example to print numbers from 5 to 15
for num in range(5, 16):
    print(num, end=' ')  #output: 5 6 7 8 9 10 11 12 13 14 15
print()  # for newline

# another example of range like printing multiples of 3 from 3 to 30
for num in range(3, 31, 3):
    print(num, end=' ')  #output: 3 6 9 12 15 18 21 24 27 30
print()  # for newline

# simple range example to print first 10 natural numbers
for num in range(11):
    print(num, end=' ')  #output: 1 2 3 4 5 6 7 8 9 10
print()  # for newline

#for loop to print single charcaters of a string
string = "Looping"
for char in string:
    print(char)
#output:
# L
# o
# o
# p
# i
# n
# g

# for loop example to accept input from user and print each character
user_input = input("Enter a string: ")
for char in user_input:
    print(char)
# If user inputs "Hello"
#output:
# H
# e
# l
# l
# o

# another example of user inpute program to print numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end=' ')
# If user inputs 5
#output: 1 2 3 4 5
print()  # for newline

# for loop to print squares of numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(f'Square of {i} is {i**2}')
# If user inputs 4
#output:
# Square of 1 is 1
# Square of 2 is 4
# Square of 3 is 9
# Square of 4 is 16