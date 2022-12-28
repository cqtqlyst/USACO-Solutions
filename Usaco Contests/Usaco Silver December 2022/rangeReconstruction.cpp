#include <vector>
#include <iostream>
using namespace std;

const int num = 300;
int arr[num];

int main() {

    int n;
    
    cin >> n;

    int max, min;
    int input;

    for (int i = 0; i<n; i++) {
        max = arr[i];
        min = arr[i];
        for (int j = i; j<n; j++) {
            cin >> input;
            if (arr[j] < min) {
                min = j;
            }
            if (arr[j] > max) {
                max = j;
            }
            if ((arr[max] - arr[min]) < input) {
                // cout << "we have reached here!\n";
                arr[j] = input;
                max = j;
            }
            // cout << "i is: " << i << " and j is: " << j << "\n";
            // for (int i = 0; i<n; i++) {
            //     cout << arr[i] << " ";
            // }
            // cout << "\n";
        }
    }

    cout << arr[0];

    for (int i = 1; i<n; i++) {
        cout << " " << arr[i];
    }

}