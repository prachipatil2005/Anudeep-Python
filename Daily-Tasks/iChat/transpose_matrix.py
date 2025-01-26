def transpose_matrix():
    try:
        # Take user input for a 2D array
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        matrix = []
        print("Enter the elements row by row:")

        # Taking input for the matrix
        for i in range(rows):
            row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
            matrix.append(row)

        # Print the original matrix
        print("\nOriginal Matrix:")
        for row in matrix:
            print(row)

        # Swap rows and columns (transpose the matrix)
        transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

        # Print the transposed matrix
        print("\nTransposed Matrix (Swapped Rows and Columns):")
        for row in transposed_matrix:
            print(row)

    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Run the function
transpose_matrix()
