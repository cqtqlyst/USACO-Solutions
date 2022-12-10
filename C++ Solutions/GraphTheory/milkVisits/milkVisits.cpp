#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;

vector<vector<int>> adj;
vector<bool> visited; 
string cowsMilk;
int num = 0;
vector<int> ans;

void dfs(int v) {
    visited[v] = true;
    ans[v] = num;
    for (int node: adj[v]) {
        if (cowsMilk[node] == cowsMilk[v]) { 
            dfs(node);
        }
    }
}

int main() {
    freopen("milkvisits.in", "r", stdin);
    freopen("milkvisits.out", "w", stdout);

    int n, m;
    cin >> n, m;
    cin >> cowsMilk;
    ans = vector<int>(n);
    adj = vector<vector<int>>(n, vector<int>(0));
    visited = vector<bool>(n);
    for (int i = 0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 0; i<n; i++) {
        dfs(i);
        num++;
    }

    for (int i = 0; i<m; i++) {
        int start, end;
        char preference;
        cin >> start >> end >> preference;
        start--; end--;
        if (ans[start] == ans[end]) {
            cout << (cowsMilk[start] == preference);
        }
        else {
            cout << "1";
        }
    }
}