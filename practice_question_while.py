#while loop practice questions
# print numbers from 1 to 100 using while loop
num = 1
while num <= 100:
    print(num, end=' ')
    num += 1 #output: 1 2 3 ... 100
print()  # for newline

# print even numbers from 1 to 100 using while loop
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1  #output: 2 4 6 ... 100
print()  # for newline

# print odd numbers from 1 to 100 using while loop
num = 1
while num <= 100:
    if num % 2 != 0:
        print(num, end=' ')
    num += 1  #output: 1 3 5 ... 99
print()  # for newline

# calculate the sum of numbers from 1 to 100 using while loop
num = 1
total_sum = 0
while num <= 100:
    total_sum += num
    num += 1
print(total_sum)  #output: 5050

# find the factorial of a number using while loop
number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)  #output: 120

# print the multiplication table of a number using while loop
number = 7
i = 1
while i <= 10:
    print(f'{number} x {i} = {number * i}')
    i += 1
#output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# print digits of a number in reverse order using while loop
number = 12345
while number > 0:
    digit = number % 10
    print(digit, end=' ')
    number //= 10
#output: 5 4 3 2 1
print()  # for newline

# check if a number is prime using while loop
num = 29
is_prime = True
i = 2
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
#output: 29 is a prime number

# print Fibonacci series up to n terms using while loop
n_terms = 10
a, b = 0, 1
count = 0
while count < n_terms:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
#output: 0 1 1 2 3 5 8 13 21 34
print()  # for newline

#print the number from 100 to 1 using while loop
num = 100
while num >= 1:
    print(num, end=' ')
    num -= 1
#output: 100 99 98 ... 1
print()  # for newline

#print the elements of the following list using while loop
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
#output:
# apple
# banana
# cherry
# date
# elderberry

#search for an element in a list using while loop
numbers = [10, 23, 45, 70, 11, 15, 90]
target = 15
index = 0
found = False
while index < len(numbers):
    if numbers[index] == target:
        found = True
        break
    index += 1
if found:
    print(f'{target} found in the list')
else:
    print(f'{target} not found in the list')
#output: 15 found in the list

# using continue statement in while loop to skip even numbers and print odd numbers
num = 1
while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    print(num, end=' ')
    num += 1
#output: 1 3 5 7 9 11 13 15 17 19
print()  # for newline

# using continue statement in while loop to skip odd numbers and print even numbers
num = 1
while num <= 20:
    if num % 2 != 0:
        num += 1
        continue
    print(num, end=' ')
    num += 1
#output: 2 4 6 8 10 12 14 16 18 20
print()  # for newline