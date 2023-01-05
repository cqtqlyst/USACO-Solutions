#include <iostream>
#include <vector>
using namespace std;

const int mx = 5000005;
int min_turns[mx] = {0, 1};
bool composite[mx] = {false};
int max_mod4[4] = {2, 1, 2, 3};

int main() {

    for (int i = 2; i<mx; i++) {
        if (!composite[i]) {
            for (int j = i; j< mx; j+=i) {
                composite[j] = true;
            }
            max_mod4[i % 4] = i;
        }
        min_turns[i] = (i - max_mod4[i % 4]) / 2 + 1;
    }

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<int> vals(n);
        vector<bool> win(n);
        int minWin = mx;
        for (int i = 0; i<n; i++) {
            cin >> vals[i];
            minWin = min(min_turns[vals[i]], minWin);
            win[i] = vals[i] % 4;
        }
        for (int i = 0; i<n; i++) {
            if (min_turns[vals[i]] == minWin) {
                if (win[i]) {
                    cout << "Farmer John" << endl;
                }
                else {
                    cout << "Farmer Nhoj" << endl;
                }
                break;
            }
        }
    }

}