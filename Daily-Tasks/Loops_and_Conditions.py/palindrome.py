

def is_palindrome(string):
    # Convert to lowercase for uniformity
    string=string.lower()
    # Compare string with its reverse
    return string==string[::-1] #sequence[start:stop:step]

string=input("Enter a string:")
if is_palindrome(string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")

    