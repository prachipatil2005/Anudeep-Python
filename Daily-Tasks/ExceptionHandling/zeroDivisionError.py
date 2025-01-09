try:
    num1 = int(input("Enter a number: "))  # Attempt to convert the first input into an integer
    num2 = int(input("Enter a second number: "))  # Attempt to convert the second input into an integer
    result = num1 / num2  # Trying to divide num1 by num2, which might cause division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # If num2 is zero, a ZeroDivisionError will be raised and this message will be shown
else:
    print(f"The division is {result}")  # If no error occurs, print the result of the division
