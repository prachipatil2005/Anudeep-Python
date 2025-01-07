# Taking input for the first set
set1 = set(map(int, input("Enter elements for set1 (separated by space): ").split()))
# Taking input for the second set
set2 = set(map(int, input("Enter elements for set2 (separated by space): ").split()))
# Find common elements between the two sets
common_elements = set1.intersection(set2)
# Output the result
if common_elements:
    print(f"The common elements between the sets are: {common_elements}")
else:
    print("There are no common elements between the sets.")
