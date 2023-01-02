#include <stdio.h>

int main(){
    int n, i, j;
    scanf("%d", &n);
    
    for (i = 0; i < 2 * n; i++){
        if (i % 2 == 0){
            for (j = 0; j < n; j++){
                if (j % 2 != 0){
                    printf(" ");
                } else {
                    printf("*");
                }
            }
            printf("\n");
        } else {
            for (j = 0; j < n; j++){
                if (j % 2 == 0){
                    printf(" ");
                } else {
                    printf("*");
                }
            }
            printf("\n");
        }
    }
    
    return 0;
}
