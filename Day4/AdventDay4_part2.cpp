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
    int final_sum = 0, current_number, match_count;
    bool numbers_phase;

    // Initialize vector to store the number of cards, start with 1 card
    vector<int> number_of_cards(1, 1);  // Start with 1 card at the first index
    int index = 0;  // Current index for processing each line

    // Read all lines from the file into a vector
    vector<string> lines;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    // Process each line of the input file
    for (const string& line : lines) {
        vector<int> winning_numbers;  // Vector to store winning numbers for each line
        numbers_phase = false;  // Reset to false before encountering '|'

        // Index for counting how many matching winning numbers we find
        match_count = 0;

        // Split the current line into words
        stringstream ss(line);
        string word;

        // Loop through all words in the line
        while (ss >> word) {
            // Phase before encountering '|', i.e., collecting winning numbers
            if (!numbers_phase && word[word.length() - 1] != ':' && isdigit(word[0])) {
                winning_numbers.push_back(stoi(word));  // Store the number in winning_numbers
            }
            // Phase after encountering '|', i.e., checking matches with winning numbers
            else if (numbers_phase && isdigit(word[0])) {
                current_number = stoi(word);  // Convert the word to a number
                // Check if the current number is in winning_numbers
                if (find(winning_numbers.begin(), winning_numbers.end(), current_number) != winning_numbers.end()) {
                    match_count++;  // Increment match count
                    // Ensure space in number_of_cards for current line matches
                    if (index + match_count >= number_of_cards.size()) {
                        // Add new card count based on previous index
                        number_of_cards.push_back(number_of_cards[index] + 1);
                    } else {
                        // Increment card count for existing entry
                        number_of_cards[index + match_count] += number_of_cards[index];
                    }
                }
            }
            // Switch to numbers phase after encountering '|'
            else if (word == "|") {
                numbers_phase = true;
            }
        }

        // Add the card count for the current line to the final sum
        final_sum += number_of_cards[index];

        // Move to the next line (increment index)
        index++;
        // Ensure we have space in the vector for the next line
        if (index >= number_of_cards.size()) {
            number_of_cards.push_back(1);  // Initialize next index with 1 card
        }
    }

    // Output the total sum of card counts
    cout << "Total sum: " << final_sum << endl;

    file.close();  // Close the input file
    return 0;
}
