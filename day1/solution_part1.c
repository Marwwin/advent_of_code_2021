#include <stdio.h>

void main(){
    FILE *fp;
    int counter = 0;
    int i = 0;
    int prev = 0;
    fp = fopen("input.txt","r");
    fscanf(fp,"%d",&i);
    prev = i;
    while (!feof (fp))
    {
        fscanf (fp, "%d", &i);   
        if (i > prev ){
            counter += 1;
        }   
        prev = i;

    }
    printf("%d\n",counter);
}