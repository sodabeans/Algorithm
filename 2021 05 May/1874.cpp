#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

vector<char> answer;
stack<int> s;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n, input = 0;
    cin >> n;
    int count = 1;
    
    for (i = 0; i < n; i++){
        cin >> input;
        while (count <= input){
//            cout << "push\n";
            s.push(count);
            count++;
            answer.push_back('+');
        }
        if (s.top() != input || input > n){
            cout << "NO\n";
            return 0;
        } else {
//            cout << "pop\n";
            s.pop();
            answer.push_back('-');
        }
    }
    
    for (i = 0; i < answer.size(); i++){
        cout << answer[i] << "\n";
    }
    
    return 0;
}
