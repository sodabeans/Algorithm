#include <stdio.h>

int main(){
    int arr[1000000];
    int n, i, j;
    
    arr[0] = 1;
    arr[1] = 1;
    
    for (i = 2; i <= 1000000; i++){
        for (j = 2 * i; j <= 1000000; j += i){
            arr[j] = 1;
        }
    }
    
    while(1){
        int count = 0;
        scanf("%d", &n);
        if (n == 0){
            break;
        }
        for (i = n + 1; i <= 2 * n; i++){
            if (arr[i] == 0){
                count++;
            }
        }
        printf("%d\n", count);
    }
    
    return 0;
}
