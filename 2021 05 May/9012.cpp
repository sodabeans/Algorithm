// 컴파일 에러 이유: strlen은 cstring에 있다.
// 틀린 이유: )) 두 개 들어왔을 때 처리를 안 해줬었음.
#include <iostream>
#include <cstring>
#include <stack>

using namespace std;

char ps[51];

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, j, T = 0;
    cin >> T;
    
    for (i = 0; i < T; i++){
        stack<char> s;
        cin >> ps;
        
        for (j = 0; j < strlen(ps); j++){
            if (ps[j] == '('){
                s.push(ps[j]);
            } else if (ps[j] == ')' && (j == 0 || s.empty())){
                s.push(ps[j]);
                break;
            } else {
                s.pop();
            }
        }
        
        if (s.empty()){
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
        
    }

    return 0;
}

