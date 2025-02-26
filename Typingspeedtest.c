#include<stdio.h>
#include<time.h>
#include<windows.h>
#include<string.h>
void delay(int milliseconds){
    Sleep(milliseconds);
}
int main(){
    char sentence[]="The quick brown fox jumps over the lazy dog";
    char userInput[100];
    clock_t start,end;
    double time_taken;
    int words =9;

    printf("Typing Speed Test\n");
    printf("Type the following sentence as quickly and accurately as possible:\n");
    printf("\"%s""\n\n",sentence);
    printf("Press ENTER to start....");
    getchar();
    start = clock();
    printf("\nNow start Typing:\n");
    gets(userInput);
    end = clock();
    time_taken = ((double)(end-start))/CLOCKS_PER_SEC;
    double wpm =(words/time_taken)*60;
    if(strcmp(sentence,userInput)==0){
        printf("\n Great! You typed correctly");
    }
    else{
        printf("\n Your typing had errors!\n");
    }
    printf(" Time Taken:%2f seconds\n",time_taken);
    printf("Typing speed:%2f WPM\n",wpm);
    return 0;
    
}