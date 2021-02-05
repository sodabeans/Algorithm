#include <stdio.h>

int main(){
    int c, N, i, j;
    
    scanf("%d", &c);
    
    for (i=0;i<c;i++){
        scanf("%d", &N);
        int sum = 0;
        int count = 0;
        int score[1000];
        double avg = 0.0;
        
        for (j=0;j<N;j++){
            scanf("%d", &score[j]);
            sum += score[j];
        }
        
        avg = (double) sum / N;
        
        for (j=0;j<N;j++){
            if (score[j] > avg){
                count++;
            }
        }
        printf("%.3lf%%\n", (double)count*100 / N);
    }
    return 0;
}
