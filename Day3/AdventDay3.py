def find_adjacent_symbol(ascii_value):
    """This function checks if the given character (by its ASCII value) 
    is NOT a digit (48-57), a decimal point (.), or a newline character.
    It returns True if the character is something other than these."""
    return(not(48 <= ascii_value <= 57) and ascii_value != 46 and ascii_value != ord('\n'))

if (__name__ == '__main__'):
    # Open the input file "input3.txt" for reading.
    with open("input3.txt", "r") as f:
        # Read all lines from the file into the 'lines' list.
        lines = f.readlines()

    number = final_sum = 0  # Initialize 'number' and 'final_sum' to 0.
    adjacent = False  # Initialize 'adjacent' to False.

    # Loop through each line in the 'lines' list.
    for i in range(len(lines)):
        adjacent = False  # Reset 'adjacent' to False for each new line.
        number = 0  # Reset 'number' to 0 for each new line.

        # Loop through each character in the current line.
        for j in range(len(lines[i])):
            # Check if the current character is a digit (using its ASCII value).
            if 48 <= ord(lines[i][j]) <= 57:
                # If it's a digit, build the 'number' by multiplying the previous 'number' by 10 and adding the current digit. This handles multi-digit numbers.
                number = number * 10 + int(lines[i][j])

                # If 'adjacent' is not yet set to True, check for adjacent symbols.
                if not adjacent:
                    # Check if not the first row.
                    if i != 0:
                        adjacent = find_adjacent_symbol(ord(lines[i-1][j]))
                        # Check the top-left diagonal.
                        if not adjacent and j != 0:
                            adjacent = find_adjacent_symbol(ord(lines[i-1][j-1]))
                        # Check the top-right diagonal.
                        if not adjacent and j != len(lines[i]) - 1:
                            adjacent = find_adjacent_symbol(ord(lines[i-1][j+1]))

                    # Check the symbol directly below the current one (if not the last row).
                    if not adjacent and i != len(lines) - 1:
                        adjacent = find_adjacent_symbol(ord(lines[i+1][j]))
                        # Check the bottom-left diagonal.
                        if not adjacent and j != 0:
                            adjacent = find_adjacent_symbol(ord(lines[i+1][j-1]))
                        # Check the bottom-right diagonal.
                        if not adjacent and j != len(lines[i]) - 1:
                            adjacent = find_adjacent_symbol(ord(lines[i+1][j+1]))

                    # Check the symbol to the right.
                    if not adjacent and j != len(lines[i]) - 1:
                        adjacent = find_adjacent_symbol(ord(lines[i][j+1]))
                    # Check the symbol to the left.
                    if not adjacent and j != 0:
                        adjacent = find_adjacent_symbol(ord(lines[i][j-1]))

            # If the current character is not a digit.
            else:
                # If 'adjacent' is True, add the current 'number' to 'final_sum'.
                if adjacent:
                    final_sum += number  # Add the number to the final sum.


                adjacent = False  # Reset 'adjacent' to False.
                number = 0  # Reset 'number' to 0 to prepare for the next number.

    # After processing all lines and numbers, print the final sum.
    print(final_sum)
