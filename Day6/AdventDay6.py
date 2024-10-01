import numpy as np

if __name__ == '__main__':
    with open("input6.txt", "r") as f:
        lines = f.readlines()

    # Extracting the time and distance values from the input file
    times = lines[0].split()[1:]      # Remove the first element from the time line
    distances = lines[1].split()[1:]  # Remove the first element from the distance line

    ways_you_can_beat = []  # Store the number of ways for each time-distance pair

    # Loop over the times and distances to compute "ways you can beat"
    for time in range(len(times)):
        count = 0  # Initialize count for each time-distance pair
        for i in range(int(times[time]) + 1):
            # Check if i * (time - i) exceeds the distance
            if i * (int(times[time]) - i) > int(distances[time]):
                count += 1
        
        # Append the count of ways for the current time-distance pair
        ways_you_can_beat.append(count)
    


    # Calculate and print the product of all ways you can beat 
    print(np.prod(ways_you_can_beat))
