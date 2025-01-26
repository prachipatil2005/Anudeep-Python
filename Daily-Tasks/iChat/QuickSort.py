import random
from collections import Counter

# Step 1: Generate a random array of 10,000 integers between -50 and +50
array = [random.randint(-50, 50) for _ in range(10000)]

# Step 2: Print the frequency distribution using Counter from collections
frequency = Counter(array)
print("Frequency Distribution of Numbers:")
for num, freq in frequency.items():
    print(f"{num}: {freq}")

# Step 3: Sorting the array using QuickSort (you can also implement MergeSort if desired)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Step 4: Sort the array using the QuickSort function
sorted_array = quicksort(array)

# Step 5: Print the sorted array (optional to limit the output to the first 20 elements for readability)
print("\nSorted Array (first 20 elements):")
print(sorted_array[:20])  # Printing the first 20 sorted elements
