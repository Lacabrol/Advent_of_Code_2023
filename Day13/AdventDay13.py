import numpy as np

def horizontal_mirror(array, index):

    mirror = True  # Assume it's a mirror unless proven otherwise

    # Loop through rows on either side of the index and compare them
    for i in range(min(index + 1, len(array) - index - 1)):  # Ensure the loop stays within bounds
        if not np.array_equal(array[index + i + 1], array[index - i]):  # Compare the rows
            mirror = False  # Set to False if any comparison fails

    return mirror  # Return True if it's a mirror, False otherwise


def vertical_mirror(array, index):

    mirror = True  # Assume it's a mirror unless proven otherwise

    # Loop through columns on either side of the index and compare them
    for i in range(min(index + 1, len(array[0]) - index - 1)):  # Ensure the loop stays within bounds
        if not np.array_equal(array[:, index + i + 1], array[:, index - i]):  # Compare the columns
            mirror = False  # Set to False if any comparison fails

    return mirror  # Return True if it's a mirror, False otherwise


if __name__ == '__main__':

    # Open and read the input file
    with open("input13.txt", "r") as file:
        lines = file.readlines()

    # Clean up each line, strip newlines, and convert each line into a list of characters
    lines = [list(line.strip()) for line in lines]

    beginning = 0  # Tracks the starting index of each array
    tab = []  # This will store the different arrays of characters
    final_sum = 0  # Initialize the final sum of valid mirror indexes

    # Loop through the lines to break them into arrays based on empty lines (lines with length < 2)
    for line in range(len(lines)):
        if len(lines[line]) == 0:  # Detect empty lines
            tab.append(np.array(lines[beginning:line]))  # Create a new array from the lines
            beginning = line + 1  # Move the beginning index to the next non-empty line

    # Add the last section of the input as a new array
    tab.append(np.array(lines[beginning:len(lines)]))

    # Loop through each array in 'tab'
    for array in tab:

        # Check for horizontal mirrors
        for i in range(len(array) - 1):  # Loop through each row (except the last one)
            if np.array_equal(array[i], array[i + 1]):  # If two consecutive rows are equal
                if horizontal_mirror(array, i):  # Check if it's part of a horizontal mirror pattern
                    final_sum += (i + 1) * 100  # Add to final_sum based on row index

        # Check for vertical mirrors
        for j in range(len(array[0]) - 1):  # Loop through each column (except the last one)
            if np.array_equal(array[:, j], array[:, j + 1]):  # If two consecutive columns are equal
                if vertical_mirror(array, j):  # Check if it's part of a vertical mirror pattern
                    final_sum += j + 1  # Add to final_sum based on column index

    # Print the final sum of all mirror matches
    print(final_sum)
