#Figure out to store values in set like 9 and 9.0 both are same or different in set
# Storing values in a set
value_set = set()
value_set.add(9)
value_set.add("9.0")
print("Set with 9 and '9.0':", value_set)
# Output: Set with 9 and '9.0': {9, '9.0'}
# Conclusion: 9 and 9.0 are treated as different values in a set

my_set = set()
my_set.add(int(input("Enter a number: ")))  # Accepting user input and adding to set
my_set.add(float(input("Enter a decimal number: ")))  # Accepting user input and adding

print("My Set:", my_set)