#include <vector>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;

unordered_map<char, int> letterMap = {
        {'a', 0},
        {'b', 1},
        {'c', 2},
        {'d', 3},
        {'e', 4},
        {'f', 5},
        {'g', 6},
        {'h', 7},
        {'i', 8},
        {'j', 9},
        {'k', 10},
        {'l', 11},
        {'m', 12},
        {'n', 13},
        {'o', 14},
        {'p', 15},
        {'q', 16},
        {'r', 17},
        {'s', 18},
        {'t', 19},
        {'u', 20},
        {'v', 21},
        {'w', 22},
        {'x', 23},
        {'y', 24},
        {'z', 25},
        {'A', 26},
        {'B', 27},
        {'C', 28},
        {'D', 29},
        {'E', 30},
        {'F', 31},
        {'G', 32},
        {'H', 33},
        {'I', 34},
        {'J', 35},
        {'K', 36},
        {'L', 37},
        {'M', 38},
        {'N', 39},
        {'O', 40},
        {'P', 41},
        {'Q', 42},
        {'R', 43},
        {'S', 44},
        {'T', 45},
        {'U', 46},
        {'V', 47},
        {'W', 48},
        {'X', 49},
        {'Y', 50},
        {'Z', 51},
    };

vector<bool> visited(52);
vector<char> letterChange(52);
int ctr;
bool foundTrue;

void findLoop(int goal, int current) {
    if (goal == current && ctr != 0) {
        foundTrue = true;
        return;
    }
    ctr++;
    int letterIndex = letterMap[letterChange[current]]; // the index of the letter that is connected
    if (letterMap[letterChange[letterIndex]] == letterIndex) { // if "changed" to itself, there is no loop
        return;
    }
    if (!visited[letterIndex]) {
        visited[letterIndex] = true;
        findLoop(goal, letterIndex);   
    }
}

int main() {
    int n;
    cin >> n;

    string first;
    string second;
    int ans;
    char firstChar;
    char secondChar;

    for (int i = 0; i<n; i++) {
        ans = 0;
        letterChange = vector<char>(52, ' '); // essentially my adjacency in a sense
        visited = vector<bool>(52, false);
        unordered_set<char> unavailable;
        ctr = 0;
        foundTrue = false;

        cin >> first >> second;
        for (int j = 0; j<first.size(); j++) {
            firstChar = first.at(j);
            secondChar = second.at(j);
            if (unavailable.find(firstChar) == unavailable.end()) {
                unavailable.insert(firstChar);
            }
            if (unavailable.find(secondChar) == unavailable.end()) {
                unavailable.insert(secondChar);
            }
            if (letterChange[letterMap[firstChar]] == ' ') { // nothing there
                if (firstChar != secondChar) {
                    ans++;
                }
                letterChange[letterMap[firstChar]] = secondChar;
            }
            else { //something there (check if it is new or same)
                if (letterChange[letterMap[firstChar] != secondChar]) { // true - diff, impossible, false - same, possible
                    ans = -1;
                    break;
                }
            }
            
        }

        int totalAvailable = 52 - unavailable.size();       

        if (ans != -1) { // if not already impossible, check for loops
            for (int j = 0; j<52; j++) {
                foundTrue = false;
                ctr = 0;
                if (letterChange[j] != ' ' && letterMap[letterChange[j]] != j) { // if it's not empty or not changed to itself
                    if (!visited[j]) {
                        findLoop(j, j);
                        if (foundTrue) {
                            if (totalAvailable > 0) {
                                ans++;
                                totalAvailable--;
                            }
                            else {
                                ans = -1;
                                break;
                            }
                        }
                    }
                }
            }
        }

        cout << ans << endl;
    }
}
