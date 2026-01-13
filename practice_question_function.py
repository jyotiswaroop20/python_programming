# wrtite a program to print the length od a list using function
def list_length(input_list):
    """Returns the length of the input list."""
    return len(input_list)
# Example usage
my_list = [10, 20, 30, 40, 50]
print("Length of the list:", list_length(my_list))  # Output: Length of the list: 5


#write a function to print the elements of a list in a single line
def print_list_elements(input_list):
    print(*input_list)  
# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_elements(my_list)  # Output: 1 2 3 4 5


# write a function to find the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) 
# Example usage
print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120



# wrtite a program to convert USD to INR using function
def usd_to_inr(usd_amount):
    """Converts USD to INR."""
    conversion_rate = 82.0  # Example conversion rate
    return usd_amount * conversion_rate
# Example usage
usd_amount = 100
inr_amount = usd_to_inr(usd_amount)
print(f"{usd_amount} USD is equal to {inr_amount} INR")  # Output: 100 USD is equal to 8200.0 INR

#write a recursive function to print sum of first n natural numbers
def sum_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_natural_numbers(n - 1)
# Example usage
n = 5
print("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))  # Output: Sum of first 5 natural numbers is: 15

#wrtite a recursive function to print all elements in a list
def print_elements_recursively(input_list, index=0):
    if index < len(input_list):
        print(input_list[index], end=' ')
        print_elements_recursively(input_list, index + 1)
# Example usage
my_list = [10, 20, 30, 40, 50]
print("Elements in the list:")
print_elements_recursively(my_list)
print()  # for newline after printing all elements