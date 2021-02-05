#include <stdio.h>

int dn(int n){
    int ret = n;
    
    while(n != 0){
        ret += (n % 10);
        n = n / 10;
    }
    
    return ret;
}

int main(){
    int arr[10001] = {0};
    int i, temp;
    
    for (i=0;i<10001;i++){
        temp = dn(i);
        if (temp <= 10001){
            arr[temp] = 1;
        }
    }
    
    for (i=1;i<10001;i++){
        if (arr[i] != 1){
            printf("%d\n", i);
        }
    }
    
    return 0;
}
