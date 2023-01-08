#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

struct cow {
    int x;
    int y;
    int r;
    int t;
};

bool comp(cow a, cow b) {
    if (a.t == b.t) {
        return a.y < b.y;
    }
    return a.t < b.t;
}


int main() {
    freopen("stampede.in", "r", stdin);
	freopen("stampede.out", "w", stdout);

    int n;
    cin >> n;

    vector<cow> cows(n);

    for (int i = 0; i<n; i++) {
        cin >> cows[i].x >> cows[i].y >> cows[i].r;
        cows[i].t = abs(cows[i].x * cows[i].r);
    }

    sort(cows.begin(), cows.end(), comp);

    int ans = n;
    int prev = cows[0].y;
    for (int i = 1; i<n; i++) {
        if (cows[i].y == prev) {
            ans--;
        }
        prev = cows[i].y;
    }

    cout << ans << endl;

}
