#include <iostream>
#include <vector>
#include <stack>
using namespace std;

const int MAX_N = 2500;

int height, width;
string building[MAX_N];
bool visited[MAX_N][MAX_N];

void floodfill(int r, int c) {
    stack<pair<int, int>> frontier;
	frontier.push({r, c});
	while(!frontier.empty()) {
		r = frontier.top().first;
		c = frontier.top().second;
		frontier.pop();

		if (r < 0 || r >= height || c < 0 || c >= width || building[r][c] == '#' || visited[r][c]) {
			continue;
        }
		visited[r][c] = true;
		frontier.push({r + 1, c});
        frontier.push({r - 1, c});
        frontier.push({r, c + 1});
        frontier.push({r, c - 1});
	}
}

int main() {
    cin >> height >> width;
    for (int i = 0; i<height; i++) {
        cin >> building[i];
    }

    int ans = 0;
    for (int i = 0; i<height; i++) {
        for (int j = 0; j<width; j++) {
            if (!visited[i][j] && building[i][j] == '.') {
                floodfill(i, j);
                ans++;
            } 
        }
    }
    cout << ans;
}