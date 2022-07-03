#include <stdio.h>
#include <limits.h>

void main(){
    FILE *fp;
    int counter, curr = 0;
    int list[2000];
    fp = fopen("input.txt","r");
    fscanf(fp,"%d",&curr);
    while (!feof (fp))
    {
        fscanf (fp, "%d", &curr);   
        list[counter] = curr;
        counter++;
    }
    
    int higher = 0;
    int prev = INT_MAX;
    for (int j= 0;j<counter-2;j++){
        int curr = list[j]+list[j+1]+list[j+2];
        if (curr>prev){
            higher++;
        }
        prev = curr;
    }
    printf("%d\n",higher);

}