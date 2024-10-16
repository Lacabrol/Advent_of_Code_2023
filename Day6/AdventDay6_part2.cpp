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
    int final_result = 0;  

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

    string time_value, distance_value, time, distance;

    // Process each pair of time and distance values
    while (time_stream >> time_value && distance_stream >> distance_value) {

        if(isdigit(time_value[0]) && isdigit(distance_value[0])) {
            // Concatenate the time and distance
            time += time_value;
            distance += distance_value;
        }

    }

    // Calculate the number of ways you can beat the condition
    for (long i = 0; i < stoul(time)+1; ++i) {
        if (i * (stoul(time) - i) > stoul(distance)) {
            final_result++;
        }
    }
    // Output the final product
    cout << final_result << endl;

    return 0;
}
