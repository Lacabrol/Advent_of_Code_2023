import math
import re

# Function to find a number surrounding a specified position in a line
def find_number(line, pos):
    # Check if the character at position `pos` is a digit (ASCII code 48 to 57)
    if not (48 <= ord(line[pos]) <= 57):
        return -1  # Return -1 if not a digit
    else:
        # Case where there is a digit before and after the current position
        if (pos != 0 and pos != len(line) - 1 and 
            48 <= ord(line[pos - 1]) <= 57 and 48 <= ord(line[pos + 1]) <= 57):
            number = re.findall('\d+', line[pos - 1:pos + 2])[0]  # Extract the number spanning the range
        # Case where there is only a digit before the current position
        elif (pos != 0 and 48 <= ord(line[pos - 1]) <= 57):
            if pos > 1:
                number = re.findall('\d+', line[pos - 2:pos + 1])[0]  # Extract a larger number if it spans more characters
            else:
                number = re.findall('\d+', line[pos - 1:pos + 2])[0]
        # Case where there is only a digit after the current position
        elif (pos != len(line) - 1 and 48 <= ord(line[pos + 1]) <= 57):
            if pos < len(line) - 2:
                number = re.findall('\d+', line[pos:pos + 3])[0]  # Extract number in range if it's a 3-digit one
            else:
                number = re.findall('\d+', line[pos:pos + 2])[0]
        # Case where the current character is a standalone digit
        else:
            number = re.findall('\d+', line[pos])[0]
        
        return int(number)  # Return the found number as an integer

# Helper function to remove specific values from a list (used to remove -1 values)
def remove_values_from_list(lst, val):
    return [value for value in lst if value != val]  # Filter out the 'val' from the list


# Main function to process the file
if __name__ == '__main__':
    # Open the input file in read mode
    with open("input3.txt", "r") as f:
        lines = f.readlines()  # Read all lines into a list

    numbers = []  # Temporary list to store numbers found near '*'
    total_sum = 0  # Variable to accumulate the sum of products

    # Loop through each line
    for i in range(len(lines)):
        numbers = []  # Reset the numbers list for each line
        # Loop through each character in the line
        for j in range(len(lines[i])):
            if lines[i][j] == '*':  # If the character is '*', look for numbers around it
                # Check the line above the current one if not at the first line
                if i != 0:
                    numbers.append(find_number(lines[i - 1], j))  # Find the number in the same column of the previous line
                    if numbers[-1] == -1:  # If the number was not found, check diagonally adjacent numbers
                        if j != 0:
                            numbers.append(find_number(lines[i - 1], j - 1))  # Check top-left diagonal
                        if j != len(lines[i]) - 1:
                            numbers.append(find_number(lines[i - 1], j + 1))  # Check top-right diagonal

                # Check the line below the current one if not at the last line
                if i != len(lines) - 1:
                    numbers.append(find_number(lines[i + 1], j))  # Find the number in the same column of the next line
                    if numbers[-1] == -1:
                        if j != 0:
                            numbers.append(find_number(lines[i + 1], j - 1))  # Check bottom-left diagonal
                        if j != len(lines[i]) - 1:
                            numbers.append(find_number(lines[i + 1], j + 1))  # Check bottom-right diagonal

                # Check the character to the right on the same line
                if j != len(lines[i]) - 1:
                    numbers.append(find_number(lines[i][j:], 1))

                # Check the character to the left on the same line
                if j != 0:
                    numbers.append(find_number(lines[i], j - 1))

            else:  # If not '*', process the collected numbers
                # Remove -1 values from the numbers list
                numbers = remove_values_from_list(numbers, -1)

                # If at least 2 valid numbers were found, compute their product and add to sum
                if len(numbers) >= 2:
                    total_sum += math.prod(numbers)

                # Reset the numbers list after processing each '*'
                numbers = []

    # Print the total sum of products found
    print(total_sum)
