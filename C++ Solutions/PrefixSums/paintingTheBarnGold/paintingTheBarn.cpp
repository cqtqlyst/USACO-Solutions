#include <vector>
#include <iostream>
#include <cstdio>

using namespace std;

const int MAX_N = 200;

int main() {
    freopen("paintbarn.in", "r", stdin);
	freopen("paintbarn.out", "w", stdout);

    int n, k;

    cin >> n >> k;

    int prefix[MAX_N][MAX_N];
    int x1, y1, x2, y2;

    for (int i = 0; i<n; i++) {
        cin >> x1 >> y1 >> x2 >> y2;

        prefix[x1][y1]++;
        prefix[x1][y2]--;
        prefix[x2][y1]--;
        prefix[x2][y2]++;
    }    

    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            if (i>0) {
                prefix[i][j] += prefix[i-1][j];
            }
            if (j>0) {
                prefix[i][j] += prefix[i][j-1];
            }
            if (i>0 && j>0) {
                prefix[i][j] -= prefix[i-1][j-1];
            }
            cout << prefix[i][j] << " ";
         }
         cout << "\n";
    }
    
}
