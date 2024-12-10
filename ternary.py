num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Use ternary operator to find the largest number
largest = num1 if num1 > num2 else num2

# Print the result
print("The largest number is:", largest)
