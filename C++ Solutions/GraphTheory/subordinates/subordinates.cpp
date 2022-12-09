#include <vector>
#include <iostream>
using namespace std;

int n;
vector<vector<int>> children;
vector<int> subTreeSize;

void dfs(int node) {

    subTreeSize[node] = 1;

    for (int child: children[node]) {

        dfs(child);
        subTreeSize[node] += subTreeSize[child];
    }

}

int main() {

    cin >> n;

    children = vector<vector<int>>(n, vector<int>(0));
    subTreeSize = vector<int>(n);

    int parent;

    for (int i = 1; i<n; i++) {
        cin >> parent;
        children[parent-1].push_back(i);
    }

    dfs(0);

    for (int i = 0; i<n; i++) {
        cout << subTreeSize[i]-1 << " ";
    }

}