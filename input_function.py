#input function in python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")
#converting age to integer and calculating year of birth
age_int = int(age)
current_year = 2026
year_of_birth = current_year - age_int
print("You were born in the year: " + str(year_of_birth))
#End of input_function.py