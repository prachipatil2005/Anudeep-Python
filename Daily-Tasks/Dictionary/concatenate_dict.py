def get_input_dict():
    n = int(input("Enter the number of key-value pairs: "))
    dic = {}
    for _ in range(n):
        key_value = input("Enter key:value pair (e.g., 1:2): ")
        key, value = key_value.split(':')  # Split the input string at the colon
        dic[int(key)] = int(value)  # Convert the key and value to integers and add to the dictionary
    return dic

all_dict = []
num_dict = int(input("How many dictionaries would you like to enter? "))
for i in range(num_dict):
    print(f"Enter data for dictionary {i+1}:")
    all_dict.append(get_input_dict())  # Call the function and append the returned dictionary

result = {}
for dic in all_dict:
    result.update(dic)

print("Concatenated Dictionary:", result)
