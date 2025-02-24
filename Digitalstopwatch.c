#include<stdio.h>
#include<windows.h>
#include<conio.h>
//Function to create adelay with countdown timer
int main(){
    int seconds = 0,milliseconds = 0;
    char key;
    int running = 0;
    printf("Digital Stopwatch\n");
    printf("Press 's' to START, 'P' to PAUSE, 'r' to RESET, and 'q' to QUIT\n");
    while (1){
        if (_kbhit()){//check if a key is pressed
        key = _getch();  
        if (key == 's')running =1;
        if (key == 'p')running =0;
        if (key == 'r'){
            running = 0;
            seconds = 0;
            milliseconds = 0;
            printf("\nStopwatch Reset!\n");
         }
        if (key == 'q')break; //Quit program
        }
    if (running){
        printf("\rTime: %2d:%2d sec" ,seconds, milliseconds/10);
        fflush(stdout);
        Sleep(100);
        milliseconds +=10;
        if (milliseconds >= 1000){
            milliseconds = 0;
            seconds++;
            
        }
    }    
    }
    printf("\nStopWatch Ended!\n");
    return 0;

}