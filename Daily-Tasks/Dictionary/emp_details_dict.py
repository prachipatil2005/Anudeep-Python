# Accept employee details from the user
employee_details = {}

employee_details["name"] = input("Enter employee name: ")
employee_details["no"] = input("Enter employee number: ")
employee_details["ID"] = input("Enter employee ID: ")
employee_details["department"] = input("Enter employee department: ")
employee_details["designation"] = input("Enter employee designation: ")
employee_details["DOJ"] = input("Enter date of joining: ")
employee_details["DOB"] = input("Enter date of birth: ")
employee_details["salary"] = float(input("Enter employee salary: "))

# Display key, value, and item
print("\nEmployee Details:")
for key, value in employee_details.items():
    print(f"{key}: {value}")
