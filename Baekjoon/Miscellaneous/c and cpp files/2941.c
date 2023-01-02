#include <stdio.h>
#include <string.h>

int main(){
    char str[101];
    scanf("%s", str);
    
    int length = strlen(str);
    int count = 0;
    int i;
    
    for (i=0; i<length; i++){
        if (str[i] == 'd' && str[i+1] == 'z' && str[i+2] == 61){
            count++;
            i += 2;
        } else if (str[i] == 'l' && str[i+1] == 'j'){
            count++;
            i++;
        } else if (str[i] == 'n' && str[i+1] == 'j'){
            count++;
            i++;
        } else if (str[i] == 'c' && (str[i+1] == 45 || str[i+1] == 61)){
            count++;
            i++;
        } else if (str[i] == 's' && str[i+1] == 61){
            count++;
            i++;
        }else if (str[i] == 'z' && str[i+1] == 61){
            count++;
            i++;
        } else if (str[i] == 'd' && str[i+1] == '-'){
            count++;
            i++;
        } else {
            count++;
        }
    }
    
    printf("%d", count);
    
    return 0;
}
