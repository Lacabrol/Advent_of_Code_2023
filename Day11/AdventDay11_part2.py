import numpy as np

if __name__ == '__main__':
    
    # Open and read the input file
    with open("input11.txt", "r") as file:
        lines = file.readlines()

    final_sum = 0
    # Convert each line into a list of characters, removing newline characters
    tab_of_lines = [list(line.strip()) for line in lines]

    # Define the large weight (1 million) for rows and columns with only '.'
    large_weight = 999999

    rows_with_dots = []  # List to store the indices of rows that are completely '.'
    columns_with_dots = []  # List to store the indices of columns that are completely '.'

    # Identify rows that consist only of '.'
    for i in range(len(tab_of_lines)):
        if all(v == '.' for v in tab_of_lines[i]):
            rows_with_dots.append(i)

    # Identify columns that consist only of '.'
    for j in range(len(tab_of_lines[0])):
        if all(tab_of_lines[i][j] == '.' for i in range(len(tab_of_lines))):
            columns_with_dots.append(j)

    # Find the coordinates of all '#' symbols in the grid
    x, y = np.where(np.array(tab_of_lines) == '#')

    # Create copies of x and y to store adjusted coordinates after adding large weights
    x_adjusted, y_adjusted = x.copy(), y.copy()

    # Adjust x coordinates based on rows with only dots
    for i in range(len(x)):
        # For each '#' symbol, add 1 million for each row with only dots that is above the current x coordinate
        x_adjusted[i] += large_weight * sum(1 for row in rows_with_dots if x[i] > row)

    # Adjust y coordinates based on columns with only dots
    for i in range(len(y)):
        # For each '#' symbol, add 1 million for each column with only dots that is to the left of the current y coordinate
        y_adjusted[i] += large_weight * sum(1 for col in columns_with_dots if y[i] > col)

    # Calculate Manhattan distances between each pair of '#' symbols
    for i in range(len(x_adjusted) - 1):
        for j in range(i + 1, len(x_adjusted)):
            # Calculate Manhattan distance using adjusted coordinates
            final_sum += abs(x_adjusted[i] - x_adjusted[j]) + abs(y_adjusted[i] - y_adjusted[j])

    # Output the final sum of distances
    print(final_sum)
