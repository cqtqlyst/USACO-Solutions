#include <vector>
#include <iostream>
#include <string>
using namespace std;

vector<vector<bool>> done;
vector<vector<int>> cost;
int n;
vector<vector<char>> inputChar;
vector<vector<int>> inputCosts;

int findCostOf(int row, int col) {
    if (done[row][col]) {
        return cost[row][col];
    }
    if (row == n-1 && inputChar[row][col] == 'R') {

    }

}

int main() {
    cin >> n;
    inputChar = vector<vector<char>>(n, vector<char>(n));
    inputCosts = vector<vector<int>>(n+1, vector<int>(n+1));

    for(int i = 0; i<n; i++) {
        string s; int c;
        cin >> s >> c;
        for (int j = 0; j<n; j++) {
            inputChar[i][j] = s[j];
        }
        inputCosts[i][n] = c;
    }

    for (int i = 0; i<n; i++) {
        int c;
        cin >> c;
        inputCosts[n][i] = c;
    }

    done = vector<vector<bool>>(n, vector<bool>(n));
    cost = vector<vector<int>>(n, vector<int>(n));

    int q;
    cin >> q;

    int row, col;
    int currentSum;

    for (int i = 0; i<q; i++) {
        cin >> row >> col;
        


        cout << currentSum << endl;
    }
}