# Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate the sum of the list
total_sum = sum(numbers)

# Print the result
print("Sum of all items in the list:", total_sum)
