#include <stdio.h>

int main(){
    int i, j;
    int n = 2;
    
    scanf("%d", &n);
    
    int weight[n];
    int height[n];
    int rank[n];
    
    for(i = 0; i < n; i++){
        scanf("%d %d", &weight[i], &height[i]);
    }
    
    for(i = 0; i < n; i++){
        rank[i] = 1;
        for(j = 0; j < n; j++){
            if(weight[i] < weight[j] && height[i] < height[j]){
                rank[i]++;
            }
        }
    }
    
    for(i = 0; i < n; i++){
        printf("%d ", rank[i]);
    }
    
    return 0;
}
