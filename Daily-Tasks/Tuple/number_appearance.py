# Taking input tuple from the user
tuplex = tuple(map(int, input("Enter the tuple elements separated by space: ").split()))
# Counting the number of times 4 appears in the tuple
count = tuplex.count(4)
# Output the result
print(f"4 appears {count} times in the tuple.")
