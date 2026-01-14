# File se data read karna
with open("example.txt", "r") as file:
    numbers = file.read().split()

total_numbers = 0
even_count = 0

print("Even numbers are:")

for num in numbers:
    num = int(num)
    total_numbers += 1

    if num % 2 == 0:
        print(num)
        even_count += 1

print("\nTotal numbers:", total_numbers)
print("Total even numbers:", even_count)