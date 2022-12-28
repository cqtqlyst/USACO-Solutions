#include <vector>
#include <iostream>
using namespace std;

int n;
vector<int> differential;
vector<vector<int>> adj;
vector<int> weights;
vector<bool> visited;
vector<int> amounts;

int generateWeightsUnder(int node) {
    visited[node] = true;
    int sum = differential[node];
    for (int i : adj[node]) {
        if (!visited[i]) {
            sum += generateWeightsUnder(i);
        }
    }
    weights[node] = sum;
    return sum;
}

int transferWeights(int node) {
    visited[node] = true;
    int amt = 0;
    for (int i: adj[node]) {
        if (!visited[i]) {
            if (weights[i] >= 0) {
                amt += transferWeights(i);
            }
        }
    }
    amt += differential[node];
    amounts[node] = amt;
    differential[node] = 0;
    for (int i: adj[node]) {
        if (!visited[i]) {
            if (weights[i] < 0) {
                
            }
        }
    }
    return amt;
}

int main() {
    cin >> n;
    differential = vector<int>(n);
    int sum = 0;
    for (int i = 0; i<n; i++) {
        cin >> differential[i];
        sum += differential[i];
    }
    sum/=n;
    for (int i = 0; i<n; i++) {
        differential[i] = differential[i] - sum;
    }
    adj = vector<vector<int>>(n);
    int a, b;
    for (int i = 0; i<n-1; i++) {
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    weights = vector<int>(n);
    visited = vector<bool>(n);
    generateWeightsUnder(0);
    visited = vector<bool>(n);
    amounts = vector<int>(n);
    // for (int i = 0; i<n; i++) {
    //     cout << differential[i] << " ";
    // }
    // cout << "\n";
    // for (int i = 0; i<n; i++) {
    //     cout << weights[i] << " ";
    // }
}