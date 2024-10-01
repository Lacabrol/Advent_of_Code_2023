import numpy as np

if __name__ == '__main__':
    with open("input6.txt", "r") as f:
        lines = f.readlines()

    # Assuming the first line contains time values and the second line contains distance values
    times = lines[0].split()
    distances = lines[1].split()

    # Remove first element from both lists 
    times.pop(0)
    distances.pop(0)

    # Concatenate the times and distances into single strings
    time = ''.join(times)
    distance = ''.join(distances)

    # Convert the concatenated strings into integers
    time = int(time)
    distance = int(distance)

    ways_you_can_beat = 0

    # Loop over possible values of i from 0 to time (inclusive)
    for i in range(time + 1):
        # Check if the product of i and (time - i) is greater than distance
        if i * (time - i) > distance:
            ways_you_can_beat += 1
    
    # Print the number of ways you can beat
    print(ways_you_can_beat)
    

