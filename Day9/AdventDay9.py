if __name__ == '__main__':
    # Open and read the input file
    with open("input9.txt", "r") as file:
        lines = file.readlines()

    final_sum = 0  # Initialize final sum to 0

    # Process each line in the file
    for line in lines:
        steps = []  # Initialize the steps list for the current line
        
        # Split the line into numbers and convert them to integers
        current_step = [int(i) for i in line.split()]
        steps.append(current_step)  # Add the first step (the original list)

        # Continue creating new steps until the last step is all zeros
        while not all(v == 0 for v in steps[-1]):  # Keep iterating until all values are 0
            new_step = []
            # Compute the differences between consecutive values in the last step
            for i in range(len(steps[-1]) - 1):
                new_step.append(steps[-1][i+1] - steps[-1][i])
            steps.append(new_step)  # Add the new step to the list

        # Reverse calculation: adjust steps by summing adjacent values starting from the bottom
        for i in range(len(steps) - 2, -1, -1):  # Start from second last step and go upwards
            # Add the last value of the current step with the last value of the next step
            steps[i].append(steps[i][-1] + steps[i+1][-1])

        # Add the first value of the first step to the final sum
        final_sum += steps[0][-1]

    # Output the final sum after processing all lines
    print(final_sum)
