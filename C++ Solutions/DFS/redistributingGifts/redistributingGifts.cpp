#include <iostream>
#include <vector>
using namespace std;

//variables

int n;
vector<vector<int>> adj;
vector<vector<bool>> valid;


//methods

void dfs(int source, int node) {
    if (valid[source][node]) {
        return;
    }
    valid[source][node] = true;
    for (int g: adj[node]) {
        dfs(source, g);
    }
}

void findAll() {
    for (int i = 1; i<=n; i++) {
        dfs(i,i);
    }
}

int main() {

    cin >> n;

    adj = vector<vector<int>>(n+1, vector<int>(0));
    valid = vector<vector<bool>>(n+1, vector<bool>(n+1));


    bool check = false;
    int val;

    for (int i = 1; i<=n; i++) {
        for (int j = 1; j<=n; j++) {
            cin >> val;
            if (val==i) {
                adj[i].push_back(val);
                check = true;
            }
            if (!check) {
                adj[i].push_back(val);
            }
        }
        check = false;
    }

    // cout << "\n";

    // for (int i = 1; i<=n; i++) {
    //     for (int j = 0; j<adj[i].size(); j++) {
    //         cout << adj[i][j] << " ";
    //     }
    //     cout << "\n";
    // }  

    // cout << "\n";

    findAll();

    // for (int i = 1; i<=n; i++) {
    //     for (int j = 1; j<=n; j++) {
    //         cout << valid[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    // cout << "\n";

    for (int i = 1; i<=n; i++) {
        for (int g: adj[i]) {
            if (valid[g][i]) {
                cout << g << "\n";
                break;
            }
        }
    }



}


