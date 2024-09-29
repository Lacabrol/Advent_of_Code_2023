if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
    
    # Initialize variables to store the first and last digits found in a line
    first = last = -1
    final_sum = 0  # To accumulate the final sum of the first and last digits

    # Process each line in the input file
    for line in lines:
        # Reset the first and last digits for each line
        last = -1
        first = -1

        # Iterate over each character in the line
        for i in range(len(line)):
            # Check if the character is a digit
            if 48 <= ord(line[i]) <= 57:  # ASCII values: '0' is 48, '9' is 57
                last = int(line[i])  # Update the last digit found
                
                # If the first digit has not been found yet
                if first == -1:
                    first = last * 10  # Set first to ten times the last digit found

        # Add the first and last digits (if found) to the final sum
        final_sum += first + last  # Add to the accumulated sum
    
    # Print the final sum
    print(final_sum)
