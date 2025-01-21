def main():
    print("Choose an option:")
    print("1. Read from file:")
    print("2. Write to file:")
    print("3. Search keywords in the file:")
    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("Invalid input! Please enter a number (1/2/3).")
        return

    file_name = "example.txt"

    if choice == 1:
        # Read data from file
        try:
            with open("example.txt", 'r') as file:
                print("\nFile contents:")
                print(file.read())
        except FileNotFoundError:
            print("File not found. Please create/write to the file first.")

    elif choice == 2:
        # Write data to file (append mode)
        data = input("Enter the text to append into the file: ")
        with open("example.txt", 'a') as file:  # Use 'a' to append
            file.write(data + "\n")  # Adding a newline for separation
        print("Data appended successfully to the file .")

    elif choice == 3:
        # Search data in file
        keyword = input("Enter the keyword to search in the file: ")
        try:
            with open("example.txt", 'r') as file:
                content = file.read()
                if keyword in content:
                    print(f"'{keyword}' found in the file.")
                else:
                    print(f"'{keyword}' not found in the file.")
        except FileNotFoundError:
            print("File not found. Please create/write to the file first.")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
