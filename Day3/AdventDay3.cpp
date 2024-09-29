#include <fstream>
#include <iostream>
#include <string>
#include <cctype>  
#include <vector>
using namespace std;

// Function to check if the character is not a digit, period, or newline
bool find_adjacent_symbol(char ch) {
    return !(isdigit(ch) || ch == '.' || ch == '\n');
}

int main() {
    ifstream file("input3.txt");  // Open the file
    if (!file.is_open()) {
        cerr << "Error opening the file!" << endl;
        return 1;
    }

    string line;
    int number = 0, final_sum = 0;
    bool adjacent = false;

    // Read all lines from the file into a vector for easy access
    vector<string> lines;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    // Iterate through each line and character in the file
    for (int i = 0; i < lines.size(); i++) {
        line = lines[i];
        adjacent = false;
        number = 0;

        for (int j = 0; j < line.length(); j++) {
            if (isdigit(line[j])) {  // If it's a digit, build the number
                number = number * 10 + (line[j] - '0');
                if (!adjacent) {
                    // Check adjacent positions (top, bottom, left, right, diagonals)
                    // Top (i > 0 to ensure we don't go out of bounds)
                    if (i > 0 && find_adjacent_symbol(lines[i - 1][j])) adjacent = true;
                    // Top-left diagonal
                    if (i > 0 && j > 0 && find_adjacent_symbol(lines[i - 1][j - 1])) adjacent = true;
                    // Top-right diagonal
                    if (i > 0 && j < line.length() - 1 && find_adjacent_symbol(lines[i - 1][j + 1])) adjacent = true;

                    // Bottom (i < lines.size() - 1 to ensure we don't go out of bounds)
                    if (i < lines.size() - 1 && find_adjacent_symbol(lines[i + 1][j])) adjacent = true;
                    // Bottom-left diagonal
                    if (i < lines.size() - 1 && j > 0 && find_adjacent_symbol(lines[i + 1][j - 1])) adjacent = true;
                    // Bottom-right diagonal
                    if (i < lines.size() - 1 && j < line.length() - 1 && find_adjacent_symbol(lines[i + 1][j + 1])) adjacent = true;

                    // Left (j > 0 to ensure we don't go out of bounds)
                    if (j > 0 && find_adjacent_symbol(line[j - 1])) adjacent = true;
                    // Right (j < line.length() - 1 to ensure we don't go out of bounds)
                    if (j < line.length() - 1 && find_adjacent_symbol(line[j + 1])) adjacent = true;
                }
            } else {  // If it's not a digit
                if (adjacent) {  // If we found adjacent symbols around the number
                    final_sum += number;
                    cout << "Number found: " << number << endl;
                }
                adjacent = false;
                number = 0;  // Reset the number after each non-digit
            }
        }

        // Handle the case where the line ends with a valid number
        if (adjacent) {
            final_sum += number;
        }
    }

    cout << "Total sum: " << final_sum << endl;
    file.close();  // Close the file

    return 0;
}
