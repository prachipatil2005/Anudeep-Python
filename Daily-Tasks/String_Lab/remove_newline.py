string = ""
while True:
    line = input("Enter a line (or type 'exit' to stop): ")
    if line == 'exit':
        break
    string += line + " "  # Add a space after each line instead of a newline

cleaned_string = string.strip()  # Remove the trailing space
print("String with space between words:", cleaned_string)
