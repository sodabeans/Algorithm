#include <stdio.h>

int main(){
    int arr[1000] = {0,};
    int i, j;
    
    arr[0] = 1;
    arr[1] = 1;
    
    for (i = 2; i <= 1000; i++){
        for (j = i * 2; j <= 1000; j++){
            if (j % i == 0){
                arr[j] = 1;
            }
        }
    }
    
    
    int n, input;
    int count = 0;
    scanf("%d", &n);
    
    for(i = 0; i < n; i++){
        scanf("%d", &input);
        if (arr[input] == 0){
            count++;
        }
    }
    
    printf("%d\n", count);
    
    return 0;
}
