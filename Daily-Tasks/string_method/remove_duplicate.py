# Taking input string from the user
input_string = input("Enter a string: ")
# Splitting the string into words
words = input_string.split()
# Using a set to remove duplicates (since sets do not allow duplicates)
unique_words = set()
# Initializing an empty list to store the result
result = []
# Loop through the words in the input string
for word in words:
    if word not in unique_words:  # Check if the word is not already in the set
        unique_words.add(word)  # Add the word to the set
        result.append(word)  # Add the word to the result list
# Join the list back into a string with spaces between words
output_string = " ".join(result)
# Displaying the result
print(f"Output: {output_string}")
