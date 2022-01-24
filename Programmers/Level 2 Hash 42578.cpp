#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string, int> map;
    
    for (auto c : clothes){
        map[c[1]] += 1;
    }
    
    for (auto m: map){
        answer *= (m.second + 1);
    }
    
    return answer - 1;
}
