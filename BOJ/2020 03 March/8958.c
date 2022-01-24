#include <stdio.h>
#include <string.h>

int main(){
    int n, i, j;
    int score = 1;
    char str[80];
    scanf("%d", &n);
    
    int sum[n];
    
    for (i=0;i<n;i++){
        scanf("%s", str);
        sum[i] = 0;
        score = 1;
        for (j=0; j < strlen(str); j++){
            if (str[j] == 'O'){
                sum[i] += score;
                score++;
            } else if (str[j] == 'X'){
                score = 1;
            }
        }
    }
    
    for (i=0;i<n;i++){
        printf("%d\n", sum[i]);
    }
    
    return 0;
}
