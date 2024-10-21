import numpy as np

if __name__ == '__main__':
    
    # Open and read the input file 
    with open("input11.txt", "r") as file:
        lines = file.readlines()

    final_sum = 0

    # Convert each line into a list of characters and remove newline characters
    tab_of_lines = [list(line.strip()) for line in lines]
    tab_of_lines_copy = np.array(tab_of_lines)  # Convert to a NumPy array for faster operations
    nb_inserted = 0  # To track the number of inserted rows/columns

    # Insert duplicate rows of '.' where the entire row consists of '.'
    for i in range(len(tab_of_lines)):
        if all(v == '.' for v in tab_of_lines[i]):  # Check if the entire row contains only '.'
            # Insert a new row of '.' at the same index
            tab_of_lines_copy = np.insert(tab_of_lines_copy, i + nb_inserted, '.', axis=0)
            nb_inserted += 1  # Track how many rows have been inserted to adjust indices

    nb_inserted = 0  # Reset for columns

    # Insert duplicate columns of '.' where the entire column consists of '.'
    for j in range(len(tab_of_lines[0])):  # Iterate over columns
        if all(tab_of_lines[i][j] == '.' for i in range(len(tab_of_lines))):  # Check entire column
            # Insert a new column of '.' at the same index
            tab_of_lines_copy = np.insert(tab_of_lines_copy, j + nb_inserted, '.', axis=1)
            nb_inserted += 1  # Track how many columns have been inserted to adjust indices

    # Find the positions of all '#' symbols in the modified array
    x, y = np.where(tab_of_lines_copy == '#')

    # Calculate Manhattan distances between each pair of '#' symbols
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            # Calculate Manhattan distance and accumulate in final_sum
            final_sum += abs(x[i] - x[j]) + abs(y[i] - y[j])

    # Output the final sum of all distances
    print(final_sum)
