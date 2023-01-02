#include <iostream>
#include <string>
#include <stack>

using namespace std;
stack<int> s;

int main(){
    //cin cout 속도 빠르게. endl보다 \n이 더 빠름.
    //single thread이기에 알고리즘 풀이에만 사용. 실무는 ㄴㄴ
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i = 0;
    int n = 0;
    int idx = 0;
    string str;
    cin >> n;
    
    for (i = 0; i < n; i++){
        cin >> str;
        // switch case는 안 됨
        if (str == "push"){
            cin >> idx;
            s.push(idx);
        } else if (str == "pop"){
            if (s.empty()){
                cout << "-1\n";
            } else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (str == "size"){
            cout << s.size() << "\n";
        } else if (str == "empty"){
            cout << s.empty() << "\n";
        } else if (str == "top"){
            if (s.empty()){
                cout << "-1\n";
            } else {
                cout << s.top() << "\n";
            }
        } else {
            break;
        }
    }
    
    return 0;
}
