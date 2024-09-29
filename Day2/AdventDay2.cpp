#include <fstream> 
#include <iostream> 
#include <string> 

using namespace std; 

// Function to find and return a number from a specific starting position in the line
unsigned int find_number(int start, string line) {
    unsigned int j = 0;  // Offset for backtracking from the start position
    int number = 0;      // Variable to hold the found number

    // Continue until a non-digit character is encountered
    while (line[start - j] >= 48 && line[start - j] <= 57) {
        // Convert the substring starting from the current position to an integer
        number = stoi(&line[start - j]);  // Convert string to integer
        j++;  // Move one character to the left
    }
    return number;  // Return the found number
}
  
int main() { 
    // Initialize color score variables
    unsigned int red = 0, green = 0, blue = 0;
    unsigned int max_red = 0, max_green = 0, max_blue = 0;
    int sum = 0;  // To accumulate the sum of valid game IDs
    int id = 0;   // To store the game ID
    
    // Open the input file for reading
    ifstream inputFile("input2.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl;  // Error message if file can't be opened
        return 1; 
    } 
    
    string line;  // Variable to hold each line of the file
    // Read each line from the input file
    while (std::getline(inputFile, line)) {
        // Reset values for each line
        id = red = green = blue = 0;
        max_red = max_green = max_blue = 0;

        // Iterate over each character in the line
        for (int i = 0; i < line.size(); i++) {
            // Check for the color "red"
            if (line.substr(i, 3) == "red") {
                red += find_number(i - 2, line);  // Find and add the number before "red"
                max_red = max(red, max_red);  // Update the maximum red score
            }
            // Check for the color "green"
            else if (line.substr(i, 5) == "green") {
                green += find_number(i - 2, line);  // Find and add the number before "green"
                max_green = max(green, max_green);  // Update the maximum green score
            }
            // Check for the color "blue"
            else if (line.substr(i, 4) == "blue") {
                blue += find_number(i - 2, line);  // Find and add the number before "blue"
                max_blue = max(blue, max_blue);  // Update the maximum blue score
            }
            // If a colon is found, assume the game ID is right before it
            else if (line[i] == ':') {
                id = find_number(i - 1, line);  // Extract the ID
            }
            // If a semicolon is found, reset all color scores
            else if (line[i] == ';') {
                red = 0;  // Reset red score
                green = 0;  // Reset green score
                blue = 0;  // Reset blue score
            }
        }

        // Check if maximum scores are within allowed limits
        if (max_red <= 12 && max_green <= 13 && max_blue <= 14) {
            sum += id;  // Add ID to sum if conditions are met
        }
    }
    cout << sum;  // Output the final sum of valid game IDs
    return 0;  
}
