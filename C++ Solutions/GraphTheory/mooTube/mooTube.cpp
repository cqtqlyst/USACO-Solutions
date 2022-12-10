#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

int n, questions;
vector<vector<pair<int, int>>> adj;
vector<bool> visited;
int threshold;
int numPossible;

void dfs(int v) {
    visited[v] = true;

    for (pair<int, int>& num: adj[v]) {
        if (!visited[num.first] && num.second>=threshold) {
            numPossible++;
            dfs(num.first);
        }
    }
}

int main() {
    freopen("mootube.in", "r", stdin);
    freopen("mootube.out", "w", stdout);

    cin >> n >> questions;

    adj = vector<vector<pair<int, int>>>(n);

    int p, q, r;
    for (int i = 0; i<n-1; i++) {
        cin >> p >> q >> r;
        p--;
        q--;
        adj[p].push_back({q, r});
        adj[q].push_back({p, r});
    }

    int k, start;
    for (int i = 0; i<questions; i++) {
        cin >> k >> start;
        start--;
        threshold = k;
        numPossible = 0;
        visited = vector<bool>(n);
        dfs(start);

        cout << numPossible << "\n";
    }

}