#include <iostream>
#include <queue>

std::queue<int> q;

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, j, n, m, test, element, temp, goal;
    int max = 0;
    int count = 0;
    cin >> test;
    
    for (i = 0; i < test; i++){
        cin >> n >> m;
        for (j = 0; j < n; j++){
            cin >> element;
            q.push(element);
            if (max < element){
                max = element;
            }
            if (j == m){
                goal = element;
            }
        }
        for (j = 0; j < n; j++){
            if (q.front() < max){
//                temp = q.front();
//                q.pop();
//                q.push(temp);
//                count++;
            } else {
//                q.pop();
//                count++;
            }
        }
    }
    
    cout << count;
    
    return 0;
}
