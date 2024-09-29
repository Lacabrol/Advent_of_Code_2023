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
    int sum = 0;  // To accumulate the final sum of products
    
    // Open the input file for reading
    ifstream inputFile("input2.txt"); 
    if (!inputFile.is_open()) { 
        cerr << "Error opening the file!" << endl;  // Error message if file can't be opened
        return 1; 
    } 
    
    string line;  // Variable to hold each line of the file
    // Read each line from the input file
    while (std::getline(inputFile, line)) {
        // Reset color scores and their maximums for each line
        red = green = blue = 0;
        max_red = max_green = max_blue = 0;

        // Iterate over each character in the line
        for (int i = 0; i < line.size(); i++) {
            // Check for the color "red"
            if (line.substr(i, 3) == "red") {
                // Update the red score based on the preceding number
                red = red + find_number(i - 2, line);
                max_red = max(red, max_red);  // Update maximum red score
            }
            // Check for the color "green"
            else if (line.substr(i, 5) == "green") {
                // Update the green score based on the preceding number
                green = green + find_number(i - 2, line);
                max_green = max(green, max_green);  // Update maximum green score
            }
            // Check for the color "blue"
            else if (line.substr(i, 4) == "blue") {
                // Update the blue score based on the preceding number
                blue = blue + find_number(i - 2, line);
                max_blue = max(blue, max_blue);  // Update maximum blue score
            }
            // If a semicolon is found, reset all color scores
            else if (line[i] == ';') {
                red = 0;   // Reset red score
                green = 0; // Reset green score
                blue = 0;  // Reset blue score
            }
        }

        // Calculate the product of maximum scores and add to the sum
        sum = sum + (max_blue * max_green * max_red);
    }

    // Output the final accumulated sum of products
    cout << sum;  
    return 0;  // Exit program
}
