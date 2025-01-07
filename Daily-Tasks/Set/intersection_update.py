# Taking input for the first set
set1 = set(map(int, input("Enter elements for set1 (separated by space): ").split()))
# Taking input for the second set
set2 = set(map(int, input("Enter elements for set2 (separated by space): ").split()))
# Remove items from set1 that are not common to both sets
set1.intersection_update(set2)
# Output the result
print(f"The updated set1 with common elements is: {set1}")
