#include <vector>
#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;


vector<vector<bool>> adj;
vector<bool> visited; //1 = true, 0 = false

int dfs(int node) {
    // cout << "reached node: " << node << "\n";
	
    visited[node] = true;

    int count = 1;

	for (int i = 0; i < adj.size(); i++) {
        if (!visited[i] && adj[node][i]) {
            count+=dfs(i);
        }
    }

    return count;
}

int main() {

    freopen("moocast.in", "r", stdin);
    freopen("moocast.out", "w", stdout);

    int n;

    cin >> n;

    vector<int> x(n);
    vector<int> y(n);
    vector<int> power(n);

    adj = vector<vector<bool>>(n, vector<bool>(n));
    visited = vector<bool>(n);

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> power[i];
    }

    int distance;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i!=j) {
                distance = ((x[i] - x[j]) * (x[i] - x[j])) + ((y[i] - y[j]) * (y[i] - y[j]));
                if (distance <= (power[i]*power[i])) {
                    adj[i][j] = true;
                    // cout << i << " " << j << " " << distance << "\n";
                }
            }
        }
    }

    // for (int i = 0; i <= n; i++) {
    //     for (int j = 0; j < adj[i].size(); j++) {
    //         cout << "node: " <<  i << " and its value at j " << adj[i][j] << "\n"; 
    //     }
    // }

    int runningMax = 0;

    for (int i = 0; i < n; i++) {
        visited = vector<bool>(n);
        runningMax = max(dfs(i), runningMax);
    }
    
    cout << runningMax << endl;

}