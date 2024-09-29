if (__name__ == '__main__'):
    # Open the input file 'input2.txt' in read mode
    with open("input2.txt", "r") as f:
        lines = f.readlines()  # Read all lines into a list

    # Initialize color score counters and their maximums
    red = blue = green = 0  
    max_red = max_blue = max_green = 0  
    
    id = -1  # To store the game ID
    final_sum = 0  # To accumulate the final sum of valid game IDs
    reset = False  # Flag to determine when to reset scores

    # Process each line in the input file
    for line in lines:
        # Reset scores for each line
        red = blue = green = 0  
        max_red = max_blue = max_green = 0  
        id = -1  # Reset game ID for the new line

        # Clean up the line: remove commas and colons, then split into words
        words = line.replace(',', '').replace(':', '').split()
        
        # Iterate over each word in the processed line
        for i in range(len(words)):
            # Check if the current word is "Game" and retrieve the ID
            if (words[i] == "Game"):
                id = int(words[i + 1])  # Set ID to the number following "Game"
            else:
                # Check for a score reset signal (if the word ends with a semicolon)
                if (words[i][len(words[i]) - 1] == ';'):
                    reset = True  # Mark to reset scores
                    words[i] = words[i].replace(';', '')  # Remove the semicolon from the word

                # Update the red score if the current word is "red"
                if (words[i] == "red"):
                    red += int(words[i - 1])  # Add the score before "red"
                    max_red = max(red, max_red)  # Update maximum red score

                # Update the green score if the current word is "green"
                elif (words[i] == "green"):
                    green = int(words[i - 1])  # Set green score directly from the previous number
                    max_green = max(green, max_green)  # Update maximum green score

                # Update the blue score if the current word is "blue"
                elif (words[i] == "blue"):
                    blue += int(words[i - 1])  # Add the score before "blue"
                    max_blue = max(blue, max_blue)  # Update maximum blue score

            # If a reset signal was detected, reset all color scores
            if (reset):
                red = blue = green = 0  # Reset scores to zero
                reset = False  # Clear reset flag

        # After processing all words, check the maximum scores for conditions
        if (max_red <= 12 and max_green <= 13 and max_blue <= 14):
            final_sum += id  # Add the game ID to the final sum if conditions are met

    # Print the final accumulated sum of valid game IDs
    print(final_sum)
