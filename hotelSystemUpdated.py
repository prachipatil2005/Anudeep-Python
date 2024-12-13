# Function to display menu and handle the choices
def display_menu():
    print("\nSelect an option:")
    print("1. Starter\n2. Main course\n3. Dessert\n4. Bill")


# Function to handle starter selection
def starter_menu(item_count):
    print("You selected Starter\n")
    print("1. Soup - ₹150")
    print("2. Salad - ₹100")
    starter_choice = int(input("Enter your choice (1/2): "))
    if starter_choice == 1:
        print("You selected Soup. Price: ₹150")
        item_count["starter"]["count"] += 1  # Increment the starter count
        item_count["starter"]["items"].append("Soup")  # Add the item to the list
        return 150
    elif starter_choice == 2:
        print("You selected Salad. Price: ₹100")
        item_count["starter"]["count"] += 1  # Increment the starter count
        item_count["starter"]["items"].append("Salad")  # Add the item to the list
        return 100
    else:
        print("Invalid choice")
        return 0


# Function to handle main course selection
def main_course_menu(item_count):
    print("You selected Main Course\n")
    print("1. Pasta - ₹300")
    print("2. Biryani - ₹350")
    main_course_choice = int(input("Enter your choice (1/2): "))
    if main_course_choice == 1:
        print("You selected Pasta. Price: ₹300")
        item_count["main_course"]["count"] += 1  # Increment the main course count
        item_count["main_course"]["items"].append("Pasta")  # Add the item to the list
        return 300
    elif main_course_choice == 2:
        print("You selected Biryani. Price: ₹350")
        item_count["main_course"]["count"] += 1  # Increment the main course count
        item_count["main_course"]["items"].append("Biryani")  # Add the item to the list
        return 350
    else:
        print("Invalid choice")
        return 0


# Function to handle dessert selection
def dessert_menu(item_count):
    print("You selected Dessert.\n")
    print("1. Ice Cream - ₹80")
    print("2. Cake - ₹120")
    dessert_choice = int(input("Enter your choice (1/2): "))
    if dessert_choice == 1:
        print("You selected Ice Cream. Price: ₹80")
        item_count["dessert"]["count"] += 1  # Increment the dessert count
        item_count["dessert"]["items"].append("Ice Cream")  # Add the item to the list
        return 80
    elif dessert_choice == 2:
        print("You selected Cake. Price: ₹120")
        item_count["dessert"]["count"] += 1  # Increment the dessert count
        item_count["dessert"]["items"].append("Cake")  # Add the item to the list
        return 120
    else:
        print("Invalid choice")
        return 0


# Main function to control the flow of the program
def hotel_order_system():
    print("Welcome To my Hotel!!!!!!!!")
    total_bill = 0

    # Initialize a dictionary to keep track of items chosen
    item_count = {
        "starter": {"count": 0, "items": []},
        "main_course": {"count": 0, "items": []},
        "dessert": {"count": 0, "items": []},
    }

    while True:
        display_menu()  # Call function to display menu
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            total_bill += starter_menu(
                item_count
            )  # Call function to handle starter selection
        elif choice == 2:
            total_bill += main_course_menu(
                item_count
            )  # Call function to handle main course selection
        elif choice == 3:
            total_bill += dessert_menu(
                item_count
            )  # Call function to handle dessert selection
        elif choice == 4:
            print("\nSummary")
            print(f"Total Bill: ₹{total_bill}")

            # Display the chosen items and counts
            print("\nItems Chosen:")
            for category in item_count:
                if item_count[category]["count"] > 0:
                    print(
                        f"{category.capitalize()} ({item_count[category]['count']}): {', '.join(item_count[category]['items'])}"
                    )

            print("Have a nice day!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

        # Ask if the user wants to continue adding more items
        continue_choice = input("\nDo you want to add more items? (yes/no): ").lower()
        if continue_choice == "no":
            print("\nFinal Bill Summary")
            print(f"Total Bill: ₹{total_bill}")

            # Display the chosen items and counts
            print("----------------")
            print("Items Chosen:")
            for category in item_count:
                if item_count[category]["count"] > 0:
                    print(
                        f"{category.capitalize()} ({item_count[category]['count']}): {', '.join(item_count[category]['items'])}"
                    )

            print("Thank you for visiting! Have a nice day!")
            break


# Calling the main function to start the program
hotel_order_system()
