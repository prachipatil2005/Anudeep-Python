# 2. Declare a square() function with one parameter.Then call the function and pass one
# number and display the square of that number .

# Function to find the square of a number
def square(num):
    return num * num  # Return the square of the number

# Taking input from the user
num = float(input("Enter a number to square: "))

# Calling the function and displaying the result
result = square(num)
print("Square of the number:", result)  # Display the result
