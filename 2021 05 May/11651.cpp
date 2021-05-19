#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> coordinates;

/*
 bool ysort(const pair<int, int> &a, const pair<int, int> &b){
    return (a.second < b.second);
}
 */

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n, x, y = 0;
    cin >> n;
    
    for (i = 0; i < n; i++){
        cin >> x >> y;
        coordinates.push_back(make_pair(y, x));
    }
    
    sort(coordinates.begin(), coordinates.end());
    
    for (i = 0; i < n; i++){
        cout << coordinates[i].second << " " << coordinates[i].first << "\n";
    }
    
    return 0;
}
