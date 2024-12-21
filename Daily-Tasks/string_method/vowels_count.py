input_string=input("Enter a string:")
# Defining the vowels (both lowercase and uppercase)
vowels="aeiouAEIOU"
vowel_count=0
# Looping through each character in the input string
for char in input_string:
    if char in vowels:
        vowel_count+=1
# Displaying the count of vowels
print(f"Vowel count:{vowel_count}")