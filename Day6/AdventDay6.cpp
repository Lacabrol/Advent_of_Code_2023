#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    ifstream file("input6.txt");  // Open the input file
    if (!file.is_open()) {
        cerr << "Error opening the file!" << endl;
        return 1;
    }

    string line;
    int final_product = 1, count, time, distance;  
    vector<int> ways_to_beat;  // Store the count of ways to beat for each pair of time-distance

    // Read all lines from the file into a vector
    vector<string> lines;
    while (getline(file, line)) {
        lines.push_back(line);
    }

    // Ensure there are at least two lines (time and distance)
    if (lines.size() < 2) {
        cerr << "Insufficient data in input file!" << endl;
        return 1;
    }

    // Read the first line as time and the second as distance
    stringstream time_stream(lines[0]);
    stringstream distance_stream(lines[1]);

    string time_value, distance_value;

    // Process each pair of time and distance values
    while (time_stream >> time_value && distance_stream >> distance_value) {
        count = 0;  // Initialize the counter for this pair

        if(isdigit(time_value[0]) && isdigit(distance_value[0])) {
            // Convert the time and distance values to integers
            time = stoi(time_value);
            distance = stoi(distance_value);

            // Calculate the number of ways you can beat the condition
            for (int i = 0; i <= time; ++i) {
                if (i * (time - i) > distance) {
                    count++;
                }
            }

            // Store the result for this pair
            ways_to_beat.push_back(count);
        }

    }

    // Multiply all the counts to get the final product
    for (int count : ways_to_beat) {
        final_product *= count;
    }

    // Output the final product
    cout << final_product << endl;

    return 0;
}
