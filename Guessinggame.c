#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main(){
    int number,guess,attempts = 0;
    //seed random number generator
    srand(time(0));
    number = rand() % 100+1;
    printf("Number guessing game\n");
}