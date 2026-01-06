#Write a program to input user first name and print the length of the name and also print the name in reverse order.
first_name = input("Enter your first name: ")
print("Length of the name:", len(first_name))
print("Name in reverse order:", first_name[::-1])
print("Hello, " + first_name + "!")
print(f"Hello, {first_name}!")


#Write a program to count $ symbols in a given string.
input_string = input("Enter a string: ")
dollar_count = input_string.count('$')
print("Number of $ symbols in the string:", dollar_count)