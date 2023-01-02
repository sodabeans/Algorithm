#include <stdio.h>

int main(){
    int arr[1000001] = {0,};
    int i;
    long long j;
    
    arr[0] = 1;
    arr[1] = 1;
    
    int m, n;
    scanf("%d %d", &m, &n);

    for (i = 2; i <= n; i++){
        for (j = 2 * i; j <= n; j += i){
            arr[j] = 1;
        }
    }
    
    for (i = m; i <= n; i++){
        if (arr[i] == 0){
            printf("%d\n", i);
        }
    }
    
    return 0;
}
