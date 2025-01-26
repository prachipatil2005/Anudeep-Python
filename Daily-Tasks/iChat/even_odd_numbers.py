def filter_even_odd():
    try:
        print("Enter 10 numbers:")
        numbers=[]
        for i in range(10):
            num=float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        even_numbers=[num for num in numbers if num%2==0]
        odd_numbers=[num for num in numbers if num%2!=0]
        print("\nEven numbers:", even_numbers)
        print("Odd numbers:", odd_numbers)
    except ValueError:
        print("Invalid input! Please enter a number.")
filter_even_odd()