#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> q;
    priority_queue<int> pq;
    int answer = 0;
    for (int i = 0; i < priorities.size(); i++){
        pq.push(priorities[i]);
        q.push(make_pair(i, priorities[i]));
    }
    
    while(!q.empty()){
        int document = q.front().first;
        int prior = q.front().second;
        if (prior == pq.top()){
            answer++;
            pq.pop();
            q.pop();
            if (document == location){
                break;
            }
        } else {
            q.push(make_pair(document, prior));
            q.pop();
        }
    }
    return answer;
}
