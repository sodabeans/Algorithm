#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int tmp_d = 0;
    vector<int> days;
    
    for (int i = 0; i < progresses.size(); i++){
        while (progresses[i] < 100){
            progresses[i] += speeds[i];
            tmp_d++;
        }
        days.push_back(tmp_d);
        tmp_d = 0;
    }
    
    int max = days[0];
    
    for (int i = 0; i < days.size(); i++){
        if (max >= days[i]){
            tmp_d++;
        } else {
            answer.push_back(tmp_d);
            tmp_d = 1;
            max = days[i];
        }
    }
    answer.push_back(tmp_d);
    
    return answer;
}
