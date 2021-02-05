#include <stdio.h>

int main(){
    int i, n;
    scanf("%d", &n);
    
    int result = 0;
    
    while(1){
        if (n % 5 == 0){
            result += n/5;
            break;
        }
        
        n -= 3;
        result++;
        
        if (n<0){
            result = -1;
            break;
        }
    }
    
    /*for (i=n/5;i>0;i--){
        if ((n-(5*i)) % 3 == 0){
            result = i + (n-(5*i)) / 3;
        }
    }
    
    if (n % 3 == 0 && (result > n/3 || result == -1)){
        result = n/3;
    }
    if (n % 5 == 0 && (result > n/5 || result == -1)){
        result = n/5;
    }*/
    
    printf("%d", result);
    
    return 0;
}
