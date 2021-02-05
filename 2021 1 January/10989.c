#include <stdio.h>

#define MAX_SIZE 10000000
#define MAX_NUM 10000

int main(){
    int i, j;
    int n = 0;
    int input = 0;
    int count[MAX_NUM + 1];
    
    scanf("%d", &n);
    
    int arr[n];
    
    for(i = 0; i < n; i++){
        arr[i] = 0;
        scanf("%d", &input);
        
        count[input]++;
    }
    
    for(i = 1; i <= MAX_NUM; i++){
        count[i] += count[i - 1];
    }
    
    for(i = 0; i < n; i++){
        arr[(count[i])] = i;
        
    }
    
    for(i = 0; i < n; i++){
        if(arr[i] != 0){
            for(j = 1; j < arr[i]; j++){
                printf("%d\n", j);
            }
        }
    }
    
    return 0;
}
