# 3. Using max() and min() functions display the maximum and minimum of 5 random
# numbers.
# from numpy import number

# Taking input from the user for 5 numbers

numbers = []
for i in range(5):
    num = float(input("Enter a number"))
    numbers.append(num)
    # Using max() and min() to find the maximum and minimum values

maxNumber = max(numbers)
minNumber = min(numbers)
# Display the maximum and minimum numbers
uniqueNumbers = set(numbers)  # Convert the list to a set to remove duplicates
if len(uniqueNumbers) < len(numbers):  # If duplicates exist, the set will be smaller
    print("Some numbers are the same.")
else:
    print("All numbers are unique.")

print("The maximium number is", maxNumber)
print("The minium number is", minNumber)
