#include<stdio.h>
#include<windows.h>
void delay(int milliseconds){
    Sleep(milliseconds);
}
/*void showTrafficLight(const char *color){
    printf("Traffic Light: %s\n",color);
}*/
void countdown(int seconds, const char *color){
    for(int i = seconds;i>0;i--){
        printf("%s -%d seconds left\n",color,i);
        Sleep(1000);
    }
}
int main(){
while(1){
    //printf("\n Press Enter to cross the road...\n");
    //getchar();
    countdown(5,"\n RED");
    printf("\nSTOP\n");
//showTrafficLight("RED");
delay(3000);
countdown(5,"\n GREEN");
printf("\nGO\n");
//showTrafficLight("GREEN");
delay(3000);
countdown(2,"\n YELLOW\n");
printf("\nSLOW\n");
//showTrafficLight("YELLOW");
delay(3000);
}
return 0;
}