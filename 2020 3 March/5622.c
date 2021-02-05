#include <stdio.h>
#include<string.h>

int main(){
    int i;
    char str[16];
    scanf("%s", str);
    
    int length = strlen(str);
    int result = length;
    
    for (i=0; i<length; i++){
        if (str[i] >= 'A' && str[i] <= 'C'){
            result += 2;
        } else if (str[i] >= 'D' && str[i] <= 'F'){
            result += 3;
        } else if (str[i] >= 'G' && str[i] <= 'I'){
            result += 4;
        } else if (str[i] >= 'J' && str[i] <= 'L'){
            result += 5;
        } else if (str[i] >= 'M' && str[i] <= 'O'){
            result += 6;
        } else if (str[i] >= 'P' && str[i] <= 'S'){
            result += 7;
        } else if (str[i] >= 'T' && str[i] <= 'V'){
            result += 8;
        } else {
            result +=9;
        }
    }
    
    printf("%d", result);
    
    return 0;
}
