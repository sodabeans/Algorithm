#include <iostream>
#include <string>
#include <deque>

using namespace std;
deque<int> d;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n, x = 0;
    string str;
    cin >> n;
    
    for (i = 0; i < n; i++){
        cin >> str;
        if (str == "push_front"){
            cin >> x;
            d.push_front(x);
        } else if (str == "push_back"){
            cin >> x;
            d.push_back(x);
        } else if (str == "pop_front"){
            if (d.empty()){
                cout << "-1\n";
            } else {
                cout << d.front() << "\n";
                d.pop_front();
            }
        } else if (str == "pop_back"){
            if (d.empty()){
                cout << "-1\n";
            } else {
                cout << d.back() << "\n";
                d.pop_back();
            }
        } else if (str == "size"){
            cout << d.size() << "\n";
        } else if (str == "empty"){
            cout << d.empty() << "\n";
        } else if (str == "front"){
            if (d.empty()){
                cout << "-1\n";
            } else {
                cout << d.front() << "\n";
            }
        } else if (str == "back"){
            if (d.empty()){
                cout << "-1\n";
            } else {
                cout << d.back() << "\n";
            }
        } else {
            break;
        }
    }
    
    return 0;
}
