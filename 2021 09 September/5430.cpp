#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <deque>

using namespace std;

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t, n, i, j, k;
    string p, L;
    cin >> t;
    
    for (i = 0; i < t; i++){
        bool reverse = false;
        bool error = false;
        deque<int> dq;
        cin >> p >> n >> L;
        
        if (n != 0) {
            L = L.substr(1, L.length() - 2);
            vector<string> result;
        
            stringstream ss(L);
            while (ss.good()) {
                string substr;
                getline(ss, substr, ',');
                result.push_back(substr);
            }
            for (j = 0; j < result.size(); j++){
                dq.push_back(stoi(result[j]));
            }
        }
        
        
        for (j = 0; j < p.length(); j++){
            if (p[j] == 'R'){
                reverse = !reverse;
            } else if (p[j] == 'D'){
                if (dq.empty()){
                    error = true;
                    break;
                } else {
                    if (reverse){
                        dq.pop_back();
                    } else {
                        dq.pop_front();
                    }
                }
            }
        }
        
        if (error) {
            cout << "error\n";
        } else if (dq.empty()){
            cout << "[]\n";
        } else {
            int sizedq = dq.size() - 1;
            cout << "[";
            if (reverse) {
                for (j = 0; j < sizedq; j++) {
                    cout << dq.back() << ",";
                    dq.pop_back();
                }
            } else {
                for (j = 0; j < sizedq; j++){
                    cout << dq.front() << ",";
                    dq.pop_front();
                }
            }
            cout << dq.front();
            dq.pop_front();
            cout << "]\n";
        }
        
    }

    return 0;
}