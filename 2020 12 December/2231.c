#include <stdio.h>

int main(){
    int n = 216; //input
    int m = 0; //digit-sum
    int i, temp;
    int sum = 0;
    
    
    scanf("%d", &n);
    
    //max number of digits is 6, so from n-54
    //also requires least value so start from least possible digit-sum
    for(i = n - 54; i <= n; i++){
        temp = i;
        sum = i;
        while (temp > 0){
            sum += temp % 10;
            temp = temp / 10;
        }
        if (sum == n){
            m = i;
            break;
        }
        if (i == n){
            m = 0;
        }
    }

    printf("%d\n", m);
   
     
    return 0;
}
