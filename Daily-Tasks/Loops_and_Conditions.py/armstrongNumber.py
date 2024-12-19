def is_armstrong(number):
    num_str=str(number)
    pow=len(num_str)
    #list comprehension with a generator expression
    '''
    This is a for loop that iterates over each character (digit) in the string num_str.
    '''
    total=sum(int(digit)**pow for digit in num_str)
    return total==number

num=int(input("Enter a number:"))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
