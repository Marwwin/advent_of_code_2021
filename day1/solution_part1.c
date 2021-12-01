#include <stdio.h>
#include <limits.h>

void main(){
    FILE *fp;
    int counter, curr = 0; 
    int prev = INT_MAX;
    fp = fopen("input.txt","r");
    while (!feof (fp))
    {
        fscanf (fp, "%d", &curr);   
        if (curr > prev ){
            counter += 1;
        }   
        prev = curr;

    }
    printf("%d\n",counter);
}