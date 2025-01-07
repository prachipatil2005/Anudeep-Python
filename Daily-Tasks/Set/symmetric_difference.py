# Taking input for the first set
set1 = set(map(int, input("Enter elements for set1 (separated by space): ").split()))
# Taking input for the second set
set2 = set(map(int, input("Enter elements for set2 (separated by space): ").split()))
# Get elements that are in set1 or set2, but not both (symmetric difference)
unique_elements = set1.symmetric_difference(set2)
# Output the result
print(f"The elements that are in set1 or set2, but not both: {unique_elements}")
