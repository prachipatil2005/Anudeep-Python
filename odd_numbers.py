# # Initialize the variables
count = 1  # To count odd numbers
odd_number = 1  # The first odd number
sum_of_odds = 0  # To store the sum of odd numbers

# Loop to generate and print the first 100 odd numbers
while count <= 100:
    print(odd_number)  # Print the current odd number
    sum_of_odds += odd_number  # Add the current odd number to the sum
    odd_number += 2  # Move to the next odd number
    count += 1  # Increment the count

# Print the sum of the first 100 odd numbers
print("\nSum of the first 100 odd numbers:", sum_of_odds)
