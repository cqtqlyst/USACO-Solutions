#include <vector>
#include <cstdio>
#include <iostream>
using namespace std;


int main() {

    freopen("lazy.in", "r", stdin);
	freopen("lazy.out", "w", stdout);

    int n, k;
    cin >> n >> k;
    int new_n = 2*n - 1;
    vector<vector<int>> field = vector<vector<int>>(new_n, vector<int>(new_n));

    int val;
    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n; j++) {
            cin >> val;
            field[i+j][n-i+j-1] = val;
        }
    }

    int start_c = n%2 == 0 ? 1 : 0;

    long long max_grass = 0;
    for (int row = 0; row<new_n; row++) {
        long long curr = 0;
        for (int r = max(row - k, 0); r <= min(row + k, new_n - 1); r++) {
			for (int c = start_c; c < min(start_c + 2 * k + 1, new_n); c++) {
				curr += field[r][c];
			}
		}

        max_grass = max(max_grass, curr);
        for (int c = start_c; c + 2 * k + 1 < new_n - 1; c += 2) {
			int add_c = c + 2 * k + 1;
			for (int r = max(row - k, 0); r <= min(row + k, new_n - 1); r++) {
				curr -= field[r][c] + field[r][c + 1];
				curr += field[r][add_c] + field[r][add_c + 1];
			}
			max_grass = max(max_grass, curr);
		}

		start_c = 1 - start_c;  
    }

    // for (int i = 0; i<new_n; i++) {
    //     for (int j = 0; j<new_n; j++) {
    //         cout << field[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    cout << max_grass << endl;

}