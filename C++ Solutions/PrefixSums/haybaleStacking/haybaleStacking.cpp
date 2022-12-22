#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    freopen("stacking.in", "r", stdin);
	freopen("stacking.out", "w", stdout);

    int n, k;
    cin >> n >> k;

    vector<int> diff(n+1);
    vector<int> arr(n+1);

    int a, b;
    for (int i = 0; i<k; i++) {
        cin >> a >> b;
        a--; b--;  
        diff[a]++;
        diff[b+1]--;
    }
    
    int sum = 0;
    for (int i = 0; i<n; i++) {
        sum+=diff[i];
        arr[i] = sum;
    }

    sort(arr.begin(), arr.end());
    cout << arr[n/2] << endl;
}