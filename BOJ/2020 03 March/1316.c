#include <stdio.h>
#include <string.h>

int func (char* str){
    int length = strlen(str);
    int i, j;
    
    for (i=0; i<length; i++){
        for (j=0; j<length; j++){
            if (str[i] == str[j] && j - i > 1 && str[j] != str [j-1]){
                return 0;
            }
        }
    }
    
    return 1;
}

int main(){
    int i;
    char str[101];
    int count = 0;
    int n;
    scanf("%d", &n);
    
    for (i=0; i<n; i++){
        scanf("%s", str);
        count += func(str);
    }
    
    printf("%d", count);
    
    return 0;
}
