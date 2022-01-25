#include <stdio.h>


int main(){
    int i;
    int sum = 0;
    
    int n;
    scanf("%d", &n);
    
    char arr[101] = {0};
    scanf("%s", arr);

    for (i=0;i<n;i++){
        sum += arr[i] - 48;
    }

    printf("%d", sum);
     
    return 0;
}
