#include <iostream>
#include <list>

using namespace std;

list<int> l;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int i, n, k = 0;
    
    cin >> n;
    cin >> k;
    
    for (i = 1; i <= n; i++){
        l.push_back(i);
    }
    
    list<int>::iterator iter = l.begin();
    
    cout << "<";
    while (l.size() != 1){
        for (i = 1; i < k; i++){
            iter++;
            if (iter == l.end()){
                iter = l.begin();
            }
        }
        cout << *iter << ", ";
        iter = l.erase(iter);
        if (iter == l.end()){
            iter = l.begin();
        }
    }
    cout << *iter << ">\n";
    
    return 0;
}
