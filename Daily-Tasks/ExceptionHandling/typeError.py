try:
    num1 = input("Enter the first number: ")  # Take input from the user for the first number
    num2 = input("Enter the second number: ")  # Take input from the user for the second number
    if not num1.isdigit() or not num2.isdigit():  # Check if either num1 or num2 is not a digit (not a number)
        raise TypeError("Error: Both inputs must be numerical!")  # If any input is not a digit, raise a TypeError
    result = int(num1) + int(num2)  # Convert num1 and num2 to integers and add them
    print(f"Result: {result}")  # Print the result of the addition
except TypeError as e:  # If a TypeError is raised (when inputs are not digits), handle it here
    print(e)  # Print the error message from the TypeError exception
