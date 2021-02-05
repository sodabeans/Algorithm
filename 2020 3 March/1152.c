#include <stdio.h>
#include <string.h>

int main(){
    int i;
    int result = 0;
    
    char str[1000001];
    gets(str);
    
    int length = strlen(str);
    
    for (i=0;i<length;i++){
        if(str[i] == ' '){
            result++;
        }
    }
    
    if (str[length - 1] == ' '){
        result--;
    }
    
    if (str[0] == ' '){
        result--;
    }
    
    printf("%d", result + 1);
    
    return 0;
}
