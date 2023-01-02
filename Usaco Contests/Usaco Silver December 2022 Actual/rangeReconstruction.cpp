#include <iostream>
#include <vector>
using namespace std;

int sgn(int val) {
    if (val < 0) {
        return -1;
    }
    else if (val > 1) {
        return 1;
    }
    return 0;
}
 
int main() {

    int n;
    cin >> n;
    vector<vector<int>> diffs(n, vector<int>(n));
    
    for (int i = 0; i<n; i++) {
        for (int j = i; j<n; j++) {
            cin >> diffs[i][j];
        }
    }

    vector<int> unique;
    unique.push_back(0);
    for (int i = 1; i<n; i++) {
        if (diffs[i-1][i] != 0) {
            unique.push_back(i);
        }
    }

    vector<int> answer(n);

    if (unique.size() > 1) {
        answer[unique[1]] = diffs[0][unique[1]];
        for (int i = 2; i<unique.size(); i++) {
            int a = unique[i-2];
            int b = unique[i-1];
            int c = unique[i];
            int sign = diffs[a][c] == diffs[a][b] + diffs[b][c] ? 1 : -1;
            answer[c] = answer[b] + (sign * sgn(answer[b] - answer[a]) * diffs[b][c]);
        }
        for (int i = 1; i<n; i++) {
            if (diffs[i-1][i] == 0) {
                answer[i] = answer[i-1];
            }
        }
    }

    for (int i = 0; i<n-1; i++) {
        cout << answer[i] << " ";
    }

    cout << answer[n-1] << endl;
}