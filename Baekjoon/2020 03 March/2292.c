#include <stdio.h>

int main(){
    int n;
    int count = 1;
    
    scanf("%d", &n);
    n--;
    
    while (n>0){
        n = n - (6*count);
        count++;
    }
    
    printf("%d", count);
    
    return 0;
}
