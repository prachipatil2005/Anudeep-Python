def find_balance_index():
    try:
        # Take user input and populate the array
        numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))

        # Loop through the array to check for the balance index
        for i in range(len(numbers)):  # Iterate through all indices
            # Calculate the sum of the left side
            left_sum = sum(numbers[:i])
            # Calculate the sum of the right side
            right_sum = sum(numbers[i+1:])

            # Check if left sum equals right sum
            if left_sum == right_sum:
                print(f"Balance Index: {i}")
                return
        print("No Balance Index exists.")
        
    except ValueError:
        print("Invalid input! Please enter numbers separated by commas.")

# Run the function
find_balance_index()
