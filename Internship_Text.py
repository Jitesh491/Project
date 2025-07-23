"""CALCULATOR

TASK 2

Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.

Perform the calculation and display the result."""

# Simple Calculator in Python

# Step 1: Take two numbers as input
num1 = float(input("Enter the first number: "))  # User types e.g. 10
num2 = float(input("Enter the second number: ")) # User types e.g. 5

# Step 2: Ask the user to choose an operation
print("\nChoose an operation:")
print(" + for Addition")
print(" - for Subtraction")
print(" * for Multiplication")
print(" / for Division")
operation = input("Enter the operation symbol (+, -, *, /): ")

# Step 3: Perform the operation using if-else
if operation == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid operation selected.")



