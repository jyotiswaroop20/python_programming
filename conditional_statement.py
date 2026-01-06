#conditional statement in Python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

#check even or odd
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

#check positive, negative or zero
z = -1
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

#multiple conditions
age = 20
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

#check divisibility
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("num is divisible by both 3 and 5")
elif num % 3 == 0:
    print("num is divisible by 3")
elif num % 5 == 0:
    print("num is divisible by 5")
else:
    print("num is not divisible by 3 or 5")

#check leap year
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#nested conditional statements
score = input("Enter your score (0-100): ")
score = int(score)
if score >= 0 and score <= 100:
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid score")