#Logical operators in Python
a = 10
b = 20
c = 30
# Using 'and' operator
if a < b and b < c:
    print("Both conditions are True: a < b and b < c")
# Using 'or' operator
if a > b or b < c:
    print("At least one condition is True: a > b or b < c")
# Using 'not' operator
if not a > b:
    print("Condition is True: not a > b")
# Combining multiple logical operators
if (a < b and b < c) or (a == 10):
    print("Combined condition is True")

# Demonstrating precedence of logical operators
if a < b or b > c and a == 10:
    print("Logical operator precedence demonstrated")
# Using parentheses to change precedence
if (a < b or b > c) and a == 10:
    print("Parentheses changed the precedence of logical operators")

# End of logical_operator.py


