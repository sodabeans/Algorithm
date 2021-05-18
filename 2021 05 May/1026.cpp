#include <iostream>
#include <algorithm>

using namespace std;

int a[51];
int b[51];

int main(){
    int i, n, answer = 0;
    scanf("%d", &n);
    
    int a[n], b[n];
    
    for (i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for (i = 0; i < n; i++){
        scanf("%d", &b[i]);
    }
    
    sort(a, a + n);
    sort(b, b + n, greater<int>());
    
    for (i = 0; i < n; i++){
        answer += a[i] * b[i];
    }
    printf("%d", answer);
    
    return 0;
}
