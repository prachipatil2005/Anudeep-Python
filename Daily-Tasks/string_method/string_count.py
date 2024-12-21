input_string = input("Enter a string: ")
# Initializing counters for uppercase, lowercase, digits, and special characters
uppercase_count=0
lowercase_count=0
digit_count=0
special_count=0
for char in input_string:
    if char.isupper():
        uppercase_count+=1
    elif char.islower():
        lowercase_count+=1
    elif char.isdigit():
        digit_count+=1
    else:
        special_count+=1
# Displaying the counts
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {digit_count}")
print(f"SpecialCase : {special_count}")
