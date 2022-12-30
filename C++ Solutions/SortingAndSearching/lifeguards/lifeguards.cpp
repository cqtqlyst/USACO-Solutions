#include <vector>
#include <set>
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct event {
    int time;
    int cowId;
    bool isStart;
};

bool operator<(const event& a, const event& b) {
	return a.time < b.time;
}

int main() {
    freopen("lifeguards.in", "r", stdin);
	freopen("lifeguards.out", "w", stdout);

    int n;
    cin >> n;

    vector<event> events;
    int l, r; 
    event ph;

    for (int i = 0; i<n; i++) {
        cin >> l >> r;
        ph.time = l;
        ph.cowId = i;
        ph.isStart = true;
        events.push_back(ph);
        ph.time = r;
        ph.cowId = i;
        ph.isStart = false;
        events.push_back(ph);
    }

    sort(events.begin(), events.end());

    vector<int> aloneTime(n);
    set<int> activeCows;
    int currTime = 0;
    int prevTime = 0;
    int totalTime = 0;

    for (const event& e: events) {
        currTime = e.time;

        if (activeCows.size() > 0) {
            totalTime += currTime - prevTime;
        }

        if (activeCows.size() == 1) {
            aloneTime[*activeCows.begin()] += currTime - prevTime;
        }

        if (e.isStart == true) {
            activeCows.insert(e.cowId);
        }
        else {
            activeCows.erase(e.cowId);
        }

        prevTime = currTime;
    }

    int minAloneTime = *min_element(aloneTime.begin(), aloneTime.end());

    cout << totalTime - minAloneTime << endl;

}
