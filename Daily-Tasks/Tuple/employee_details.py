# Taking input for employee details
employee1 = tuple(input("Enter employee 1 details (name, ID, department, salary): ").split(","))
employee2 = tuple(input("Enter employee 2 details (name, ID, department, salary): ").split(","))
employee3 = tuple(input("Enter employee 3 details (name, ID, department, salary): ").split(","))
# Storing the employee tuples in a list
employees = [employee1, employee2, employee3]
# Iterating through the employee tuples and printing details
for employee in employees:
    print(f"\nEmployee Name: {employee[0]}")
    print(f"Employee ID: {employee[1]}")
    print(f"Department: {employee[2]}")
    print(f"Salary: {employee[3]}")
