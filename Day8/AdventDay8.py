import re

if __name__ == '__main__':
    # Open and read the input file
    with open("input8.txt", "r") as file:
        lines = file.readlines()

    # Initialize starting parameters
    current_node = 'AAA'  # Start at node 'AAA'
    nb_steps = 0          # Step counter
    current_index = 0     # Index to track the movement in the instruction string

    # Clean and format the network lines
    for n_line in range(2, len(lines)):
        # Use regex to clean non-alphabetic characters and keep only node names
        words = re.findall(r'[a-zA-Z]+', lines[n_line])
        lines[n_line] = words  # Store cleaned line back to the list
    
    # Convert the network data into a list of node connections
    network = lines[2:]  # Start from line 2 since first two lines are not part of the network
    instruction_string = lines[0].strip()  # Instructions for navigating the network

    # Continue traversing the network until you reach node 'ZZZ'
    while current_node != 'ZZZ':
        # Find the current node in the network and get its neighbors
        for row in network:
            if row[0] == current_node:  # Match the current node
                # Depending on the instruction (L/R), choose the next node
                if instruction_string[current_index] == 'L':
                    current_node = row[1]  # Move to the left node
                else:
                    current_node = row[2]  # Move to the right node
                break

        # Increment steps and move to the next instruction
        nb_steps += 1
        current_index += 1

        # If we exceed the length of the instruction string, loop back to the start
        if current_index == len(instruction_string):
            current_index = 0  # Reset the instruction index when reaching the end of instructions

    # Output the total number of steps taken
    print(nb_steps)
