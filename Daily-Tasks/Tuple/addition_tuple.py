# Taking input tuple from the user
tuples_list = []
n = int(input("Enter the number of tuples: "))
for i in range(n):
    temp_tuple = tuple(map(int, input(f"Enter the elements of tuple {i+1} separated by space: ").split()))
    tuples_list.append(temp_tuple)
# Calculating the sum of numbers in the given tuples
sum_tuple = sum([sum(tup) for tup in tuples_list])
# Output the result
print(f"The sum of the numbers in the given tuples is: {sum_tuple}")
