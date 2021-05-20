// using upper bound and lower bound
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, m, n = 0;
    vector<int>::iterator lower, upper;
    
    cin >> n;
    int a[n];
    for (i = 0; i < n; i++){
        cin >> a[i];
    }
    vector<int> v (a, a + n);
    sort(v.begin(), v.end());
    
    cin >> m;
    int input = 0;
    for (i = 0; i < m; i++){
        cin >> input;
        lower = lower_bound(v.begin(), v.end(), input);
        upper = upper_bound(v.begin(), v.end(), input);
        cout << upper - lower << " ";
    }
    
    return 0;
}
