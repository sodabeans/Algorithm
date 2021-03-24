#include <stdio.h>

int change (int num){
    int result = ((num % 10) * 100) + (((num/10) % 10)* 10) + ((num/100) % 10);
    
    return result;
}


int main(){
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    
    int r1 = change(num1);
    int r2 = change(num2);
    
    if (r1 >= r2){
        printf("%d", r1);
    } else {
        printf("%d", r2);
    }
    

    return 0;
}
