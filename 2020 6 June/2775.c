#include <stdio.h>

int main(){
    int arr[15][15];
    int i, j;
    
    for (i=0;i<15;i++){
        arr[0][i] = i;
    }
    
    for (i=1;i<15;i++){
        arr[i][0] = arr[i-1][0];
        for(j=1;j<15;j++){
            arr[i][j] = arr[i-1][j] + arr[i][j-1];
        }
    }
    
    int t;
    int k, n;
    scanf("%d", &t);
    
    for (i=0; i<t;i++){
        scanf("%d", &k);
        scanf("%d", &n);
        printf("%d\n", arr[k][n]);
    }
    
    return 0;
}
