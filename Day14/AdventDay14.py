import numpy as np

if __name__ == '__main__':
    # Open and read the input file
    with open("input14.txt", "r") as file:
        lines = file.readlines()
    
    # Convert each line into a list of characters and store in a 2D NumPy array
    lines = [list(line.strip()) for line in lines]  # Remove newline characters
    lines = np.array(lines)  # Convert to NumPy array for easier manipulation
    
    # Rotate the array 90 degrees counterclockwise to process each column as a row
    lines = np.rot90(lines)
    final_sum = 0  # Initialize the final sum
    
    # Process each line (formerly column) in the rotated array
    for nb_line in range(lines.shape[0]):
        next_emplacement = 0  # Track the next position to place 'O'
        
        for i in range(lines.shape[1]):
            if lines[nb_line][i] == 'O':  # If current cell contains 'O'
                lines[nb_line][i] = '.'  # Clear the current position
                lines[nb_line][next_emplacement] = 'O'  # Move 'O' to the next available position
                next_emplacement += 1  # Update the next available position for 'O'
            
            elif lines[nb_line][i] == '#':  # If current cell contains '#'
                next_emplacement = i + 1  # Update next emplacement to the position after '#'

    # Rotate the array back to its original orientation
    lines = np.rot90(lines, 3)
    
    # Calculate the final sum based on the count of 'O' in each row
    for row_index in range(lines.shape[0]):
        # Count occurrences of 'O' in the current row
        o_count = np.where(lines[row_index] == 'O')[0].shape[0]
        
        # Multiply the count of 'O' by the row's reverse index (for weighted sum)
        final_sum += o_count * (lines.shape[0] - row_index)
        
    # Output the final result
    print(final_sum)
