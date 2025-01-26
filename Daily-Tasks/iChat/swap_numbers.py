def swap_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2= float(input("Enter second number: "))
        print(f"Before swapping: num1={num1} and num2={num2}")
        num1, num2 = num2, num1
        print(f"After swapping: num1={num1} and num2={num2}")
    except ValueError:
        print("Invalid input! Please enter a number.")
swap_numbers()