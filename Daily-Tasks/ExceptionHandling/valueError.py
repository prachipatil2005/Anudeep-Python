try:
    num = int(input("Enter a number: "))  # Attempt to convert the user input to an integer
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")  # If input is not a valid integer, display an error message
else:
    print(f"The number is {num}")  # If input is a valid integer, print the number
