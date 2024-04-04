import addition
import subtraction
import multiplication
import division


def get_user_input():
    """Function to ask the user for input for calculator."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            return num1, num2, operation
        except ValueError:
            print("Please enter valid numeric input.")


def calculator(num1, num2, operation):
    """Function to perform the calculator operation based on user input."""
    if operation == '+':
        return addition.addition_function(num1, num2)
    elif operation == '-':
        return subtraction.substration_fuction(num1, num2)
    elif operation == '*':
        return multiplication.Multiplication_fuction(num1, num2)
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return division.division_function(num1, num2)
    else:
        return "Invalid operation"


# Get user input
num1, num2, operation = get_user_input()

# Perform operation
result = calculator(num1, num2, operation)

# Output result
print("Result:", result)
