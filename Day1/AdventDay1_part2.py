if (__name__ == '__main__'):
    # Open the input file and read all lines
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    # Initialize variables to hold first and last values
    first = last = -1  
    final_sum = 0  # Variable to accumulate the final sum

    # Dictionary mapping word literals to their corresponding numeric values
    literals = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    
    # Process each line from the file
    for line in lines:
        last = -1  # Reset last value for each line
        first = -1  # Reset first value for each line
        
        # Iterate over each character in the line
        for i in range(len(line)):
            litteral = -1  # Initialize litteral to -1 (not found)

            # Check if the character is a digit
            if 48 <= ord(line[i]) <= 57:  # ASCII values for digits 0-9
                last = int(line[i])  # Update last to the integer value of the digit
                if first == -1:  # If first has not been set yet
                    first = last * 10  # Set first to the current digit multiplied by 10
            
            # Check if the substring matches any literal word
            else:
                for word, num in literals.items():
                    # Check if the substring matches the word literal
                    if line[i:i + len(word)] == word:
                        last = num  # Update last to the corresponding numeric value
                        if first == -1:  # If first has not been set yet
                            first = last * 10  # Set first to the current number multiplied by 10
                        
        # Add the values of first and last to the final sum
        final_sum += first + last
    
    # Print the accumulated sum
    print(final_sum)
