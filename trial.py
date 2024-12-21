# # a = int(input("Enter your age: "))

# # # If statement no: 1
# # if a % 2 == 0:
# #     print("a is even")

# # # End of If statement no: 1

# # # If statement no: 2
# # if a >= 0:  # Age should not be negative
# #     if a >= 18:
# #         print("You are above the age of consent")
# #         print("Good for you")
# #     else:
# #         print("You are below the age of consent")
# # else:
# #     print("You are entering an invalid negative age")
# # # End of If statement no: 2

# # print("End of Program")

# # while True:
# #     # Loop body (executed at least once)
# #     print("This simulates a do-while loop")
# #     user_input = input("Continue? (y/n): ")
# #     if user_input.lower() != 'y':
# #         break

# # i=1
# # while(i<6):
# #     print(i)
# #     i+=1
# # for i in range(8):
# #     pass
# # i = 0
# # while i < 5:
# #     print(i)
# #     i += 1

# #Q. Create an application for online food ordering system

# print("Welcome to our Restaurant!\n")
# print("We are delighted to serve you. Explore our menu and place your order.\n")

# # Menu items with their prices
# starters = {'Soup': 100, 'Paneer tikka': 140, 'Garlic bread': 200}
# main_course = {'Biryani': 200, 'Butter chicken': 200, 'Pav bhaji': 170}
# desserts = {'Brownie': 200, 'Cake': 400,'Gulab jamun': 80}
# drinks = {'Coffee': 50, 'Juice': 100,'Lassi': 60,'Masala chai': 40,}

# # Total bill variable
# total_bill = 0

# # Dictionary to store ordered items
# ordered_items = {}

# def order_category(category, items):
#     print("\nSelect a dish from category:", category)
#     for item, price in items.items():
#         print(f"{item}: Rs.{price}")

#     while True:
#         item = input("\nEnter the item you want to order (or type 'done' to stop): ").capitalize()
        
#         if item == 'Done':  # Stop ordering for this category
#             break
#         elif item in items:  # If the item is available in the category
#             global total_bill
#             quantity = int(input(f"Enter the quantity for {item}: "))
#             item_total = items[item] * quantity
#             total_bill += item_total  # Add the price to the total bill

#             # Add to ordered items
#             if item in ordered_items:
#                 ordered_items[item]['quantity'] += quantity
#                 ordered_items[item]['total_price'] += item_total
#             else:
#                 ordered_items[item] = {'price': items[item], 'quantity': quantity, 'total_price': item_total}

#             print(f"{item} added to your order. Current total: Rs.{total_bill}")
#         else:
#             print("Sorry, that item is not on the menu.")

# while True:
#     print("\nPlease select a category:")
#     print("1. Starters")
#     print("2. Main Course")
#     print("3. Desserts")
#     print("4. Drinks")
#     print("Type 'done' to finish your order.")
#     choice = input("\nEnter your choice (1/2/3/4): ")

#     if choice == '1':
#         order_category('Starters', starters)
#     elif choice == '2':
#         order_category('Main Course', main_course)
#     elif choice == '3':
#         order_category('Desserts', desserts)
#     elif choice == '4':
#         order_category('Drinks', drinks)
#     elif choice == 'done':
#         break
#     else:
#         print("Invalid choice. Please select a valid option.")

#     # Ask if the customer wants to order more
#     more_order = input("\nDo you want to order more items? (yes/no): ").lower()
#     if more_order != 'yes':
#         break

# # Final bill
# print("\nYour final bill:")
# print(f"{'Item':<15}{'Price':<10}{'Quantity':<10}{'Total':<10}")
# print("-" * 45)
# for item, details in ordered_items.items():
#     print(f"{item:<15}Rs.{details['price']:<10}{details['quantity']:<10}Rs.{details['total_price']:<10}")
# print("-" * 45)
# print(f"{'Grand Total:':<35}Rs.{total_bill}")
# print("\nThank you for your order!")




# def func(num1,num2):
#     if num1==0:
#        num1 = num2 
#     else:
#         return func(num1-1,num1+num2)

# func(4,7)
# [(i, j) for i in range(2) for j in range(i, i+2)]
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# result = [sublist[:2] for sublist in list_of_lists]
# print(result)  # Output: [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
result=[y + x for x in range(2) for y in range(2)] 
print(result)