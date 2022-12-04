#include <iostream>
#include <vector>
#include <cstdio> 
#include <cmath> 
using namespace std;

//variables

int n;
vector<int> x;
vector<int> y;
vector<vector<bool>> connected;
vector<bool> visited;


//methods

int dfs(int num) {
    visited[num] = true;

    int count = 1;

    // for (int i = 0; i<n; i++) {
    //     cout << visited[i] << " ";
    // }
    // cout << "\n";

    for (int i = 0; i<n; i++) {
        // cout << "visited: " << visited[i] << " connected: " << connected[n][i] << "\n";
        if (!visited[i] && connected[num][i]) {
            // cout << "got to run dfs \n";
            count+=dfs(i);
        }
        // cout << "visited is " << visited[i] << " and connected is " << connected[n][i] << "\n";
    }
    return count;
}

bool valid(int value) {
    
    connected = vector<vector<bool>>(n+1, vector<bool>(n+1));

    // for (int i = 0; i<n; i++) {
    //     for (int j = 0; j<n; j++) {
    //         if (connected[i][j]) {
    //             cout << "1 ";
    //         }
    //         else {
    //             cout << "0 ";
    //         }
    //     }
    //     cout << "\n";
    // }

    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            int distance = ((x[i] - x[j]) * (x[i] - x[j])) + ((y[i] - y[j]) * (y[i] - y[j])); //actually distance squared cus i don't want to deal with doubles
            // cout << distance << " and the value we are comparing to " << value << "\n";
            if (distance <= value) {
                connected[i][j] = true;
            }
        }
    }
    
    // for (int i = 0; i<n; i++) {
    //     for (int j = 0; j<n; j++) {
    //         if (connected[i][j]) {
    //             cout << "1 ";
    //         }
    //         else {
    //             cout << "0 ";
    //         }
    //     }
    //     cout << "\n";
    // }

    // cout << "\n";

    visited = vector<bool>(n+1);

    // for (int i = 0; i<n; i++) {
    //     cout << visited[i] << " ";
    // }
    // cout << "\n";

    // cout << "this is the dfs(0) " << dfs(0) << "\n";

    if (dfs(0) == n) {
        return true;
    }
    else {
        return false;
    }
}

int main() {

    freopen("moocast.in", "r", stdin);
    freopen("moocast.out", "w", stdout);

    cin >> n;

    x = vector<int>(n+1);
    y = vector<int>(n+1);
    connected = vector<vector<bool>>(n+1, vector<bool>(n+1));
    visited = vector<bool>(n+1);

    for (int i = 0; i<n; i++) {
        cin >> x[i] >> y[i];
    }

    long low = 0;
    long high = INT32_MAX;
    long sol = high;

    while (low <= high) {
        long mid = low + (high - low) / 2;
        // cout << mid << "\n";
        if (valid(mid)) {
            // cout << "this is a valid value" << mid << "\n";
            high = mid-1;
            sol = min(mid, sol);
        }
        else {
            low = mid+1;
        }
    }

    cout << sol << endl;

}