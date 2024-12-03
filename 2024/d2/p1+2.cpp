#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

bool is_safe(const vector<int>& report) {
    int length = report.size();

    if (length < 2) {
        return true;  
    }

    bool increasing = true;
    bool decreasing = true;

    for (int i = 0; i < length - 1; i++) {
        int diff = report[i + 1] - report[i];

        
        if (diff < 1 || diff > 3) {
            return false;  
        }

        
        if (diff > 0) {
            decreasing = false;
        } else if (diff < 0) {
            increasing = false;
        }
    }

    return increasing || decreasing;
}


bool can_become_safe_with_one_removal(const vector<int>& report) {
    int length = report.size();

    
    for (int i = 0; i < length; i++) {
        vector<int> modified_report;
        for (int j = 0; j < length; j++) {
            if (j != i) {
                modified_report.push_back(report[j]);
            }
        }

        if (is_safe(modified_report)) {
            return true;  
        }
    }

    return false;  
}


void check_reports(const string& filename) {
    ifstream file(filename);
    string line;
    int safe_count = 0;

    
    while (getline(file, line)) {
        vector<int> report;
        stringstream ss(line);
        int number;

        
        while (ss >> number) {
            report.push_back(number);
        }

        
        if (is_safe(report) || can_become_safe_with_one_removal(report)) {
            safe_count++;
        }
    }

    cout << "Number of safe reports: " << safe_count << endl;
}

int main() {
    
    string filename = "input.txt";

    
    check_reports(filename);

    return 0;
}
