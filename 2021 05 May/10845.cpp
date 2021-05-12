#include <iostream>
#include <string>
#include <queue>

using namespace std;

queue<int> q;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string str;
    int i, n, idx = 0;
    cin >> n;
    
    for (i = 0; i < n; i++){
        cin >> str;
        if (str == "push"){
            cin >> idx;
            q.push(idx);
        } else if (str == "pop"){
            if (q.empty()){
                cout << "-1\n";
            } else {
                cout << q.front() << "\n";
                q.pop();
            }
        } else if (str == "size"){
            cout << q.size() << "\n";
        } else if (str == "empty"){
            cout << q.empty() << "\n";
        } else if (str == "front"){
            if (q.empty()){
                cout << "-1\n";
            } else {
                cout << q.front() << "\n";
            }
        } else if (str == "back"){
            if (q.empty()){
                cout << "-1\n";
            } else {
                cout << q.back() << "\n";
            }
        } else {
            break;
        }
    }
    return 0;
}
