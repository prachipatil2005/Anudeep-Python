def calculate_total_meal_cost(base_cost, tax_rate, tip_percentage):
    """
    Calculate the total cost of a meal including tax and tip.

    Parameters:
    - base_cost (float): The base cost of the meal.
    - tax_rate (float): The tax rate as a percentage (e.g., 10 for 10%).
    - tip_percentage (float): The tip percentage (e.g., 15 for 15%).

    Returns:
    - float: The total cost of the meal.
    """
    tax_amount = (tax_rate / 100) * base_cost  # Calculate tax
    tip_amount = (tip_percentage / 100) * base_cost  # Calculate tip
    total_cost = base_cost + tax_amount + tip_amount  # Calculate total
    return total_cost

# Input from user
base_cost = float(input("Enter the base cost of the meal: "))
tax_rate = float(input("Enter the tax rate (in %): "))
tip_percentage = float(input("Enter the tip percentage (in %): "))

total_cost = calculate_total_meal_cost(base_cost, tax_rate, tip_percentage)
print(f"The total cost of the meal is: ${total_cost:.2f}")
