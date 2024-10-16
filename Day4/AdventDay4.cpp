#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>  

using namespace std;

int main() {
    ifstream file("input4.txt");  // Open the input file
    if (!file.is_open()) {
        cerr << "Error opening the file!" << endl;
        return 1;
    }

    string line;
    int final_sum = 0, matches, current_number;
    bool numbers_phase, begin_phase;

    // Read all lines from the file into a vector
    vector<string> lines;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    // Process each line
    for (const string& line : lines) {
        vector<int> winning_numbers;  // Reset for each line
        numbers_phase = false;
        begin_phase = false;
        matches = -1;

        // Split the line into words
        stringstream ss(line);
        string word;

        while (ss >> word) {
            // Phase before encountering '|'
            if (!numbers_phase && word[word.length()-1] != ':' && isdigit(word[0])) {
                winning_numbers.push_back(stoi(word));
            } 
            // Phase after encountering '|'
            else if (numbers_phase && isdigit(word[0])) {
                current_number = stoi(word);
                // Check if the current number is in the winning numbers
                if (find(winning_numbers.begin(), winning_numbers.end(), current_number) != winning_numbers.end()) {
                    matches++;
                }
            } 
            // Switch to numbers phase after encountering '|'
            else if (word == "|") {
                numbers_phase = true;
            }
        }

        // Calculate the sum based on matches
        if (matches != -1) {
            final_sum += (1 << matches);  // 2^matches
        }
    }

    // Output the final sum
    cout << "Total sum: " << final_sum << endl;

    file.close();  // Close the input file
    return 0;
}
