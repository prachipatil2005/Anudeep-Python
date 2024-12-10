# 1. Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.

# Function to divide two numbers


def div(num1, num2):
    if num1 != 0:
        return num1 / num2  # Return the division result
    else:
        return "cannot divisible my zero"  # Handle division by zero
# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Calling the function and displaying the result
result = div(num1, num2)
print(result)
