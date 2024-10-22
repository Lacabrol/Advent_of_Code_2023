from itertools import product
import re

def valid_grouping(s, instructions):

    # Find all groups of consecutive '#' using regex
    groups = [match.group() for match in re.finditer(r'#+', s)]
    
    # Check if the number of groups and their sizes match the expected sequence
    return len(groups) == len(instructions) and all(len(group) == size for group, size in zip(groups, instructions))


def generate_possibilities(row, instructions):
    # Find all indices of the '?' symbol in the string
    question_indices = [i for i, char in enumerate(row) if char == '?']

    # Generate all combinations of '.' and '#' for the positions of '?'
    combinations = product('.#', repeat=len(question_indices))

    # Store all valid strings that satisfy the adjacency constraints
    valid_strings = []

    # Replace '?' in the string with each combination
    for combo in combinations:
        # Convert the input string into a list (since strings are immutable)
        temp_str = list(row)
        
        # Replace each '?' with the corresponding character from the combination
        for idx, replacement in zip(question_indices, combo):
            temp_str[idx] = replacement
        
        # Join the list back into a string
        candidate_str = ''.join(temp_str)
        
        # Check if the candidate string satisfies the adjacency constraints
        if valid_grouping(candidate_str, instructions):
            valid_strings.append(candidate_str)

    return valid_strings

if __name__ == '__main__':

    # Open and read the input file 
    with open("input12.txt", "r") as file:
        lines=file.readlines()
    # Test the function with example inputs
    final_sum=0
    instructions=[]
    row = ''

    for line in lines:
        words = line.split()
        row = words[0]
        instructions = [int (i) for i in words[1].split(',')]
        possibilities = generate_possibilities(row, instructions)
    
        # Output the valid possibilities
        final_sum += len(possibilities)

    print(final_sum)