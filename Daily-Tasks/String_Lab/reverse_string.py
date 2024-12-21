string=input("Enter a string:")
# Split the string into words, reverse the order, and join them with a space
reversed_string=' '.join(reversed(string.split()))
# Print the reversed words
print("Reversed words:",reversed_string)