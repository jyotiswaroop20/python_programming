#Write a programn to check even or odd number.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


#Write a program to find greatest among three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3
print("The greatest number is:", greatest)


#Write a program to find greatest among four numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
if (a >= b) and (a >= c) and (a >= d):
    greatest = a
elif (b >= a) and (b >= c) and (b >= d):
    greatest = b
elif (c >= a) and (c >= b) and (c >= d):
    greatest = c
else:
    greatest = d
print("The greatest number is:", greatest)


#Write a program to check if a number is multiple of 7 or not.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is a multiple of 7.")
else:
    print(f"{num} is not a multiple of 7.")

        