if __name__ == '__main__':
    # Open and read the file "input5.txt"
    with open("input5.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file

    lowest_number = 0  # Variable to track the lowest number encountered
    current_number = 0  # Variable to store the current number being processed
    almanac = [[]]  # List of lists to store instructions, where each inner list represents a group of instructions
    almanac_index = 0  # Index to keep track of the current group in the almanac

    # Process each line from the input file, skipping the first and last lines
    for line in range(1, len(lines) - 1):
        words = lines[line].split()  # Split the line into individual words/numbers
        if len(words) == 3:
            # If the line contains exactly 3 words, treat it as an instruction (action, lower_bound, range)
            almanac[almanac_index].append([int(words[0]), int(words[1]), int(words[2])])
        elif len(words) != 0:
            # If the line is not empty but doesn't have 3 words, start a new group of instructions
            almanac.append([])  # Add a new empty group to the almanac
            almanac_index += 1  # Increment the index to move to the new group

    # The first line of the input file contains the seed numbers (ignoring the first element)
    seed_numbers = lines[0].split()  # Split the first line into words/numbers
    seed_numbers.pop(0)  # Remove the first number (assuming it's not needed)
    
    # Reset the almanac index for seed number processing
    almanac_index = 0  
    
    # Iterate through each seed number
    for seed in seed_numbers:
        current_number = int(seed)  # Convert the seed string to an integer
        
        # Process each set of instructions (almanac_line) for the current seed number
        for almanac_line in almanac:
            for instruction in almanac_line:
                # Check if current_number falls within the instruction's defined range
                if instruction[1] <= current_number <= instruction[1] + instruction[2]:
                    # If it falls within the range, modify current_number according to the action in instruction[0]
                    current_number = instruction[0] + (current_number - instruction[1])
                    break  # Once an instruction matches, stop processing this almanac line

        # Update the lowest_number if necessary
        if current_number < lowest_number or lowest_number == 0:
            lowest_number = current_number  # Keep track of the lowest number seen
    
    # Output the lowest resulting number after processing all seed numbers
    print(lowest_number)
