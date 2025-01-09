# Print menu options for the user to choose from
print("Choose an operation:")
print("1.Try except")  # Option 1: Try-except block
print("2.Try multiple except")  # Option 2: Try-except with multiple except blocks
print("3.Try except else")  # Option 3: Try-except with an else block
print("4.Finally")  # Option 4: Try-except with a finally block
print("5.Try single except")  # Option 5: Try-except with a single except for multiple exceptions
print("6.Raising exception")  # Option 6: Raising an exception manually

choice = int(input("Enter your choice:"))  # Taking input from user to choose the operation

# Case 1: Try-except block to handle errors
if choice == 1:
    try:
        num1 = int(input("Enter first number: "))  # Take input for the first number
        num2 = int(input("Enter second number: "))  # Take input for the second number
        result = num1 / num2  # Perform division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")  # Catch division by zero error

# Case 2: Try-except with multiple except blocks
elif choice == 2:
    try:
        num1 = int(input("Enter first number: "))  # Take input for the first number
        num2 = int(input("Enter second number: "))  # Take input for the second number
        result = num1 / num2  # Perform division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")  # Catch division by zero error
    except ValueError:
        print("Error: Invalid input. Please enter integers.")  # Catch invalid input error

# Case 3: Try-except with an else block
elif choice == 3:
    try:
        num1 = int(input("Enter first number: "))  # Take input for the first number
        num2 = int(input("Enter second number: "))  # Take input for the second number
        result = num1 / num2  # Perform division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")  # Catch division by zero error
    else:
        print("Result:", result)  # Print the result if no exception occurs

# Case 4: Try-except with a finally block
elif choice == 4:
    try:
        num1 = int(input("Enter first number: "))  # Take input for the first number
        num2 = int(input("Enter second number: "))  # Take input for the second number
        result = num1 / num2  # Perform division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")  # Catch division by zero error
    finally:
        print("Finally block executed.")  # This will always execute whether an exception occurs or not

# Case 5: Try-except for multiple exceptions using a single except block
elif choice == 5:
    try:
        num1 = int(input("Enter first number: "))  # Take input for the first number
        num2 = int(input("Enter second number: "))  # Take input for the second number
        result = num1 / num2  # Perform division
    except (ZeroDivisionError, ValueError):  # Catch both ZeroDivisionError and ValueError
        print("Error: Invalid input or division by zero.")

# Case 6: Raising an exception manually
elif choice == 6:
    try:
        raise Exception("This is an exception")  # Manually raise an exception
    except Exception as e:
        print("An error occurred:", e)  # Catch and print the raised exception
