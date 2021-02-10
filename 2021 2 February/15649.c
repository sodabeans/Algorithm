#include <stdio.h>

int dfs(int n, int m){
    //Depth First Search without repetition of tree nodes
    //So the visited nodes must be ignored on the next path
    int i, j;
    int num = 0;
    int visited[9] = {0, };

    if (m == 1) {
        for (i = 1; i <= n; i++){
            printf("%d\n", i);
        }
    } else {
        for(i = 1; i <= n; i++){
            
            for (j = 1; j <= m; j++){
                
            }
            printf("\n");
        }
    }
    
    return num;
}

int main(){
    int n = 0; //n까지의 자연수
    int m = 0; //m개 고르기

    scanf("%d %d", &n, &m);
    
    dfs(n, m);
    
    return 0;
}

