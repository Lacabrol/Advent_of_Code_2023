#include <fstream>  
#include <iostream> 
#include <string>   
using namespace std; 

int main() 
{ 
    int first, last; // Variables to hold the first and last digit found
    int sum = 0;     // Variable to accumulate the final sum
    ifstream inputFile("input.txt"); // Open the input file for reading
    if (!inputFile.is_open()) { // Check if the file opened successfully
        cerr << "Error opening the file!" << endl; // Error message if file can't be opened
        return 1; 
    } 
    
    string line; // Variable to hold each line of the file
    while (std::getline(inputFile, line)) // Read each line from the input file
    {
        first = last = -1; // Reset the first and last variables for each line

        // Iterate over each character in the line
        for(int i = 0; i < line.length(); i++) {
            // Check if the character is a digit
            if(line[i] >= 48 && line[i] <= 57) {
                last = stoi(&line[i]); // Convert the digit character to an integer

                // Reduce last to a single-digit number
                while(last >= 10) { // While last has more than one digit
                    last = last / 10; // Divide by 10 to shift down
                }

                // If the first digit has not been set yet
                if(first == -1) {
                    first = last * 10; // This logic is flawed; sets first incorrectly
                }
            }  
        }

        // Add the values of first and last to the total sum
        sum = sum + first + last; 
    }
    // Output the final sum
    cout << sum; 
    return 0; // Exit program
}
