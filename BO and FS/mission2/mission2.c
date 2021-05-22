#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

#define GUESSSIZE 20
#define BUFSIZE 0x10000

char guess[GUESSSIZE];

void do_guess(){
    printf("Guess the flag!\n");
    scanf("%20s", guess);
    printf("Your guess was: ");
    printf(guess);
}


int main(){
    char flag_space[BUFSIZE];
    FILE *f = NULL;
    char *flag_file = "./flag";

    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    f = fopen(flag_file, "rb");
    if (f == NULL){
        puts("[!] Flag not found!\n");
        exit(-1);
    }
    memset(flag_space, '\0', BUFSIZE);

    if (fread(&flag_space[1680], BUFSIZE-1680, 1, f) < 0){
        puts("[!] I was not able to read the flag!");
        exit(-1);
    }

    do{
        do_guess();
    } while (strncmp(guess, &flag_space[1680], GUESSSIZE));

    printf("Great Job!\n");

    exit(0);
}
