#include <stdio.h>
#include <limits.h>

struct Tuple {
    int count;
    int *list[INT_MAX];
};

struct Tuple get_input(){
    FILE *fp;
    int counter = 0;
    int i = 0;
    int list[INT_MAX];
    printf("hepp");

    fp = fopen("day1/input.txt","r");
    fscanf(fp,"%d",&i);
    printf("hepp");

    while (!feof (fp))
    {
        fscanf (fp, "%d", &i);   
        list[counter] = i;
        counter++;
    }
    printf("hepp");

    struct Tuple tuple = {counter,{list}};

    printf("hepp");

    return tuple;
}
void main(){
    printf("hepp");

    struct Tuple in = get_input();
    printf("%d",in.count);

}