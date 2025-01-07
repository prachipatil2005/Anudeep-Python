# Accept a list of strings from the user
colors = input("Enter colors separated by space: ").split()

# Traverse the list in reverse order and print the elements with their original index
print("\nTraverse the list in reverse order:")
for index in range(len(colors)-1, -1, -1):
    print(f"{colors[index]} (original index: {index})")
