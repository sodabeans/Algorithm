#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> map;
    
    for (auto person: completion){
        map[person] += 1;
    }
    
    for (auto person: participant){
        map[person] -= 1;
        if (map[person] < 0){
            return person;
        }
    }
}
