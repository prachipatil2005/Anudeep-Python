text=input("Enter a string:")
# Defining a string containing all vowels (both lowercase and uppercase)
vowels="aeiouAEIOU"
# Dictionary to store the count of each vowel
vowels_count={}
for char in text:
    # Checking if the character is a vowel

    if char in vowels:
        vowels_count[char]=vowels_count.get(char,0)+1
print("Vowel count:",vowels_count)
total_vowels=sum(vowels_count.values())
# Printing the total count of vowels in the text
print("Total vowels:", total_vowels)
