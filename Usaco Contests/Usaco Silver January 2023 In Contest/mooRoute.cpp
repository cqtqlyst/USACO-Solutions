#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    vector<int> arr(n);
    cin >> n;
    for (int i = 0; i<n; i++) {
        cin >> arr[i];
    }

    string ans = "";
    int currentIndex = 0;

    int ctr = 0;


    while (ctr<10E5) {
        if (currentIndex == 0) {
            if (arr[0] != 0) {
                currentIndex++;
                arr[0]--;
                ans.append("R");
            }
            else {
                break;
            }
        }
        else if(currentIndex == n) {
            if (arr[n-1] != 0) {
                currentIndex--;
                arr[n-1]--;
                ans.append("L");
            }
            else {
                break;
            }
        }
        else {
            if (arr[currentIndex-1] == 0 && arr[currentIndex] == 0) {
                break;
            }
            else {
                if (arr[currentIndex] > arr[currentIndex-1]) { // go right
                    ans.append("R");
                    ans[currentIndex]--;
                    currentIndex++;
                }
                else { // go left
                    ans.append("L");
                    ans[currentIndex-1]--;
                    currentIndex--;
                }
            }
        }
        ctr++;

        cout << ctr;

    }

    cout << ans << endl;
    
}