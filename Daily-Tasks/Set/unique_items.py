# Taking input for the first set
set1 = set(map(int, input("Enter elements for set1 (separated by space): ").split()))
# Taking input for the second set
set2 = set(map(int, input("Enter elements for set2 (separated by space): ").split()))
# Get unique items from both sets (union of both sets)
unique_items = set1.union(set2)
# Output the result
print(f"The unique items from both sets are: {unique_items}")
