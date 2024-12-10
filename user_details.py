# # Function to accept user details
# def acceptUserDetails():
#     # Input user details
#     userName = input("Enter your name: ")
#     userAge = int(input("Enter your age: "))
#     userAddress = input("Enter your address: ")
#     userAccountNumber = int(input("Enter account number: "))

#     # Call display function with collected details
#     displayUserDetails(userName, userAge, userAddress, userAccountNumber)

# # Function to display user details
# def displayUserDetails(userName, userAge, userAddress, userAccountNumber):
#     # Display user details
#     print("\nUser Details:")
#     print(f"Name: {userName}")
#     print(f"Age: {userAge}")
#     print(f"Address: {userAddress}")
#     print(f"Account Number: {userAccountNumber}")

# # Call the function to accept and display user details
# acceptUserDetails()
#---------------------------------------------------------
# Declare global variables
# userName = ""
# userAge = 0
# userAddress = ""
# userAccountNumber = 0


# # Function to accept user details and assign them to global variables
# def acceptUserDetails():
#     global userName, userAge, userAddress, userAccountNumber

#     # Input user details and assign to global variables
#     userName = input("Enter your name: ")
#     userAge = int(input("Enter your age: "))
#     userAddress = input("Enter your address: ")
#     userAccountNumber = int(input("Enter account number: "))

#     # Call the display function to show user details
#     displayUserDetails()


# # Function to display user details using global variables
# def displayUserDetails():
#     # Display user details using the global variables
#     print("\nUser Details:")
#     print("Name:", userName)
#     print("Age:", userAge)
#     print("Address:", userAddress)
#     print("Account Number:", userAccountNumber)


# # Call the function to accept and display user details
# acceptUserDetails()
#---------------------------------------------------------
# Declare global variables
UserName = ""
UserAge = 0
UserAddress = ""
UserAccountNumber = 0
UserBalance = 0  # Variable to store the account balance

# Function to accept user details and assign them to global variables
def acceptUserDetails():
    global UserName, UserAge, UserAddress, UserAccountNumber, UserBalance
    
    # Input user details and assign to global variables
    UserName = input("Enter your name: ")
    UserAge = int(input("Enter your age: "))
    UserAddress = input("Enter your address: ")
    UserAccountNumber = int(input("Enter account number: "))
    UserBalance = float(input("Enter initial deposit amount: "))  # Initial deposit
    
    # Call the function to display user details
    displayUserDetails()

# Function to display user details using global variables
def displayUserDetails():
    global UserName, UserAge, UserAddress, UserAccountNumber, UserBalance
    # Display user details
    print("\nUser Details:")
    print("Name:", UserName)
    print("Age:", UserAge)
    print("Address:", UserAddress)
    print("Account Number:", UserAccountNumber)
    print("Account Balance: $", UserBalance)

# Function to perform deposit
def deposit():
    global UserBalance
    depositAmount = float(input("\nEnter amount to deposit: $"))
    UserBalance += depositAmount  # Add the deposit amount to the balance
    print(f"${depositAmount} deposited successfully!")
    displayUserDetails()  # Show updated balance

# Function to perform withdraw
def withdraw():
    global UserBalance
    withdrawAmount = float(input("\nEnter amount to withdraw: $"))
    
    if withdrawAmount <= UserBalance:
        UserBalance -= withdrawAmount  # Deduct the withdraw amount from the balance
        print(f"${withdrawAmount} withdrawn successfully!")
    else:
        print("Insufficient balance!")
    
    displayUserDetails()  # Show updated balance

# Main function to manage transactions
def transaction():
    # Accept user details
    acceptUserDetails()
    
    while True:
        print("\nChoose an action:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Exit")
        
        # Input choice for transaction
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == 1:
            deposit()  # Call the deposit function
        elif choice == 2:
            withdraw()  # Call the withdraw function
        elif choice == 3:
            print("Exiting... Thank you!")
            break  # Exit the loop
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

# Start the transaction function
transaction()
