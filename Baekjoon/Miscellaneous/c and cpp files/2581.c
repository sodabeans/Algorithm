#include <stdio.h>

int main(){
    int arr[10000] = {0,};
    int i, j;
    
    arr[0] = 1;
    arr[1] = 1;
    
    for (i = 2; i <= 10000; i++){
        for (j = i * 2; j <= 10000; j++){
            if (j % i == 0){
                arr[j] = 1;
            }
        }
    }
    
    int m, n;
    int least = 0;
    int sum = 0;
    scanf("%d %d", &m, &n);
    
    for (i = n; i >= m; i--){
        if (arr[i] == 0){
            sum += i;
            least = i;
        }
    }
    
    if (least == 0 && sum == 0){
        printf("-1");
    } else {
        printf("%d\n%d", sum, least);
    }
    
    return 0;
}
