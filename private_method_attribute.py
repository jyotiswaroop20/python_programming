# Private methods and attributes in Python OOP

"""
In Python, private methods and attributes are indicated by prefixing with double underscores (__).
This triggers name mangling, making them harder to access from outside the class.

Private members are not truly private (can still be accessed with _ClassName__attribute),
but they signal that they should not be used directly from outside the class.

This promotes encapsulation and data hiding in OOP.
"""

class BankAccount:
    """A simple bank account class demonstrating private attributes and methods."""

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance     # Private attribute
        self.__account_number = self.__generate_account_number()  # Private method call

    def __generate_account_number(self):
        """Private method to generate account number."""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        """Public method to check balance."""
        return self.__balance

    def __calculate_interest(self):
        """Private method to calculate interest (not accessible directly)."""
        return self.__balance * 0.05  # 5% interest

    def show_account_info(self):
        """Public method to display account information."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance}")
        # Can call private method internally
        interest = self.__calculate_interest()
        print(f"Estimated Annual Interest: ${interest:.2f}")

# Creating and using the bank account
account = BankAccount("John Doe", 1000)

# Using public methods
account.deposit(500)
print(f"Current balance: ${account.get_balance()}")

# Displaying account info (calls private methods internally)
account.show_account_info()

# Trying to access private attribute directly (not recommended)
# This works but breaks encapsulation
print(f"\nDirect access to private balance: ${account._BankAccount__balance}")

# Private method can't be called directly
# account.__calculate_interest()  # This would raise AttributeError