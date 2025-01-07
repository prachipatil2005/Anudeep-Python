# Accept a list of numbers from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Check if there are at least two numbers
if len(numbers) < 2:
    print("Please enter at least two numbers for comparison.")
else:
    # Check if all numbers are the same
    if all(num == numbers[0] for num in numbers):
        print("All numbers entered are the same.")
    else:
        # Initialize variables for the largest and smallest number
        largest = numbers[0]
        smallest = numbers[0]

        # Loop through the list to find the largest and smallest numbers
        for num in numbers:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num

        # Print the result
        print("Largest number:", largest)
        print("Smallest number:", smallest)
