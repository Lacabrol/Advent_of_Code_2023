if __name__ == '__main__':
    # Open and read the input file
    with open("input9.txt", "r") as file:
        lines = file.readlines()

    final_sum = 0  # Initialize the final sum to 0

    # Process each line in the file
    for line in lines:
        steps = []  # Initialize steps for the current line

        # Split the line into integers
        current_step = [int(i) for i in line.split()]
        steps.append(current_step)  # Append the first step

        # Keep creating steps until the last step is all zeros
        while not all(v == 0 for v in steps[-1]):
            current_step = []  # Initialize the next step
            # Compute the differences between consecutive values in the previous step
            for i in range(len(steps[-1]) - 1):
                current_step.append(steps[-1][i + 1] - steps[-1][i])
            steps.append(current_step)  # Append the new step to steps

        # Reverse the process to adjust steps by inserting at the beginning
        for i in range(len(steps) - 2, -1, -1):
            # Insert at the beginning the difference of the first element of the current step
            steps[i].insert(0, steps[i][0] - steps[i + 1][0])

        # Add the first value of the first step to the final sum
        final_sum += steps[0][0]

    # Output the final sum after processing all lines
    print(final_sum)
