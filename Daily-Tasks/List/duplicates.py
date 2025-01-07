# Accept a list from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find duplicates using a set
duplicates = []
seen = set()

# Loop through the list and find duplicates
for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.add(num)

# Print the result
print("Duplicate values:", duplicates)
