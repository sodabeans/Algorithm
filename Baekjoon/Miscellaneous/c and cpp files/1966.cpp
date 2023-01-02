#include <iostream>
#include <queue>

using namespace std;

priority_queue<int> pq;
queue<pair<int, int>> q;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i = 0;
    int j, test, priority;
    int m = 0;
    int n = 0;
    pair<int, int> temp = make_pair(0, 0);
    
    cin >> test;
    
    while(i < test){
        int count = 0;
        cin >> n >> m;
        for (j = 0; j < n; j++){
            cin >> priority;
            pq.push(priority);
            q.push(make_pair(priority, j));
        }
        while (!pq.empty()){
            if (pq.top() != q.front().first){
                temp = q.front();
                q.pop();
                q.push(temp);
    //            cout << "priority not equal\n";
            } else {
                if (q.front().second == m){
                    count++;
                    cout << count << "\n";
                    i++;
                }
                q.pop();
                pq.pop();
                count++;
    //            cout << "priority equal\n";
            }
        }
    }
    
    return 0;
}
