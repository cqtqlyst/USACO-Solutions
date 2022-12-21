#include <iostream>
#include <vector>
#include <queue>
using namespace std;

//uses bfs, will get to it later

int main() {

    vector<string> map;
    pair<int, int> start;
    pair<int, int> endPoint;
    vector<vector<bool>> visited;
    string finalPath;
    int finalPathSize;

    int rows, columns;
    cin >> rows >> columns;

    map = vector<string>(rows);
    visited = vector<vector<bool>>(rows, vector<bool>(columns));

    for (int i = 0; i<rows; i++) {
        cin >> map[i];
        for (int j = 0; j<columns; j++) {
            if (map[i][j] == 'A') {
                start.first = i;
                start.second = j;
            }
            if (map[i][j] == 'B') {
                endPoint.first = i;
                endPoint.second = j;
            }
        }
    }

    queue<pair<int, int>> q;



}