#include <stdio.h>
#include <stdlib.h>

void read_motd(char * buf){
    FILE *f_ptr;
    if ((f_ptr = fopen("./motd.txt", "rb")) == NULL) {
        printf("Error opening file");
        exit(1);
    }
    fseek(f_ptr, 0, SEEK_END);
    long fsize = ftell(f_ptr);
    printf("File size: %ld\n", fsize);
    fseek(f_ptr, 0, SEEK_SET);
    fread(buf, 1, fsize, f_ptr);
    fclose(f_ptr);
}

void print_motd(){
    char buf[581];
    read_motd(buf);
    buf[580]='\0';
    printf("%s", buf);
}

int main(int argc, char * argv[]){
    int number;
    unsigned int size;
    char * memo = NULL;
    
    print_motd();

    while (1){
        printf("\n1) Create memo.\n2) Edit memo.\n3) Print memo.\n4) Delete memo.\n5) Quit\n\nInsert your choice > ");
        scanf("%d", &number);
        fflush(stdin);
        switch (number)
        {
        case 1:
            if (memo != NULL){
                printf("Delete the memo first!\n");
            }else{
                printf("Memo size > ");
                scanf("%d", &size);
                fflush(stdin);
                memo = (char *) malloc(size+1);
                printf("Memo content > ");
                fgets(memo, size, stdin);
                fflush(stdin);
            }
            break;
        case 2:
            if (memo != NULL){
                printf("Memo content > ");
                fgets(memo, size, stdin);
                fflush(stdin);
            }else{
                printf("Initialize the memo first!\n");
            }
            break;
        case 3:
            if (memo != NULL){
                printf("%s", memo);
            }else{
                printf("Initialize the memo first!\n");
            }
            break; 
        case 4:
            if (memo != NULL){
                free(memo);
                memo=NULL;
            }else{
                printf("Initialize the memo first!\n");
            }
            break; 
        default:
            printf("\nThanks for using Aladude, Bye!\n");
            return 0;
            break;
        }
    }
    return 0;
}
