# Accept a list from the user and the length of the first part
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
split_length = int(input("Enter the length of the first part of the list: "))

# Split the list into two parts
first_part = numbers[:split_length]
second_part = numbers[split_length:]

# Print the result
print("First part:", first_part)
print("Second part:", second_part)
