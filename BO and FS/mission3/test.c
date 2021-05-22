#include <stdio.h>
#include <stdlib.h>


void my_print(){
    char msg[48];
    int size = 48+1;
    unsigned int i;

    while (size>48){
        printf("Enter the lenght of your message > ");
        scanf("%d", &size);
        fflush(stdin);
    }
    i = 0;
    printf("Enter your message\n");
    getc(stdin); // spare \n
    while (i<size){
        printf("i: %d \tsize:%d\n", i, size);
        msg[i]=getc(stdin);
        if (msg[i] == '\n'){
            msg[i] = '\0';
            break;
        }
        i++;
    }
    printf("%s\n", msg);
    fflush(stdin);
}

int main(int argc, char * argv[]){
    my_print();
    return 1;
}