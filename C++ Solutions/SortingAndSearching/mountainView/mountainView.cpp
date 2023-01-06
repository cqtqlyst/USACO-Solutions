#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

struct mount {
    int pos;
    int neg;
};

bool cmp(mount a, mount b) {
    if (a.neg == b.neg) {
        return a.pos > b.pos;
    }
    return a.neg < b.neg;
}

const int MAX_N = 1e5;
mount arr[MAX_N];

int main() {
    freopen("mountains.in", "r", stdin);
	freopen("mountains.out", "w", stdout);

    int n;
    cin >> n;
    int x, y;
    for (int i = 0; i<n; i++) {
        cin >> x >> y;
        arr[i].pos = x + y;
        arr[i].neg = x - y;
    }

    sort(arr, arr+n, cmp);
    int mxPos = -1;
    int ans = 0;

    for (int i = 0; i<n; i++) {
        if (arr[i].pos > mxPos) {
            ans++;
            mxPos = arr[i].pos;
        }
    }

    cout << ans << endl;

}