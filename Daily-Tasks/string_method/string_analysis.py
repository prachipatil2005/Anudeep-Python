input_string=input("Enter a string:")
# Initializing counters for characters, digits, and symbols
char_count=0
digit_count=0
symbol_count=0
# Looping through each character in the input string
for char in input_string:
    if char.isalpha():# Checking if the character is a letter
        char_count+=1
    elif char.isdigit():# Checking if the character is a digit
        digit_count+=1
    else:
        symbol_count+=1 # If the character is neither a letter nor a digit, it is a symbol
print(f"Chars={char_count} Digits={digit_count} Symbols={symbol_count}")
    

