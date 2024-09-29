#include <fstream> 
#include <iostream> 
#include <string> 
using namespace std; 

int main() 
{ 
    int first, last, tmp;  // Declare variables to hold the first and last numbers, and a temporary variable for processing
    int sum = 0;           // Variable to accumulate the total sum
    ifstream inputFile("input.txt"); // Open the input file
    if (!inputFile.is_open()) {       // Check if the file opened successfully
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 
    
    string line; // Variable to hold each line from the file
    // Read each line from the input file
    while (std::getline(inputFile, line))
    {
        first = -1; // Initialize first to -1 (not found)
        last = -1;  // Initialize last to -1 (not found)

        // Iterate over each character in the line
        for (int i = 0; i < line.length(); i++) {
            // Check if the character is a digit
            if (line[i] >= 48 && line[i] <= 57) {  // ASCII values for '0' to '9'
                tmp = stoi(&line[i]);  // Convert the character to an integer
                while (tmp > 10) {      // Reduce tmp to the last digit
                    tmp = tmp / 10;     // Continuously divide by 10
                }
            }
            // Check for word literals for numbers
            else if (i + 3 < line.length() && line.substr(i, 4) == "zero") tmp = 0;
            else if (i + 2 < line.length() && line.substr(i, 3) == "one") tmp = 1;
            else if (i + 2 < line.length() && line.substr(i, 3) == "two") tmp = 2;
            else if (i + 4 < line.length() && line.substr(i, 5) == "three") tmp = 3;
            else if (i + 3 < line.length() && line.substr(i, 4) == "four") tmp = 4;
            else if (i + 3 < line.length() && line.substr(i, 4) == "five") tmp = 5;
            else if (i + 2 < line.length() && line.substr(i, 3) == "six") tmp = 6;
            else if (i + 4 < line.length() && line.substr(i, 5) == "seven") tmp = 7;
            else if (i + 4 < line.length() && line.substr(i, 5) == "eight") tmp = 8;
            else if (i + 3 < line.length() && line.substr(i, 4) == "nine") tmp = 9;
            else {
                tmp = -1; // Reset tmp if no match found
            }

            // If a valid number (digit or word) was found
            if (tmp != -1) {  
                last = tmp;  // Update last to the current number
                // If first hasn't been set, set it to the current number multiplied by 10
                if (first == -1) {
                    first = tmp * 10; // Store first as ten times the current number
                }
            }
        }
        
        // Update total sum
        sum = sum + first;
        sum = sum + last;
    }
    // Output the final accumulated sum
    cout << sum;  
    return 0; 
}
