#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int admin;
    int list[4];
    int size;
} wishlist;

void print_wlist(wishlist wlist){
    int i;

    printf("\nWish list:\n");
    for (i = 0; i < wlist.size; i++){
        printf("%d) ", i+1);
        switch (wlist.list[i])
        {
        case 1:
            printf("Ploy Stetion 5.\n");
            break;
        case 2:
            printf("SuperPasqal1.\n");
            break;
        case 3:
            printf("Xknox.\n");
            break;
        case 4:
            printf("More pop ups.\n");
            break;
        case 5:
            printf("Easter Egg.\n");
            break;                       
        default:
            printf("EMPTY SLOT.\n");
            break;
        }
    }
}

void admin_message(){
    char msg[48];
    int size = 48+1;
    unsigned int i;

    while (size>48){
        printf("Enter the lenght of your message > ");
        scanf("%d", &size);
        fflush(stdin);
    }
    printf("Enter the message > ");
    i = 0;
    getc(stdin); // spare \n
    while (i<size){
        msg[i]=getc(stdin);
        if (msg[i] == '\n'){
            msg[i] = '\0';
            break;
        }
        i++;
    }
    fflush(stdin);
    printf("Got it: %s\nThanks cap.\n", msg);
    return;
}

int main(int argc, char * argv[]){
    int menu_choice, index, gift;
    wishlist wlist;
    
    wlist.admin=0;

    printf("           __   ______    __      __  __              __     \n          /  | /      \\  /  |    /  |/  |            /  |    \n  ______  $$/ /$$$$$$  |_$$ |_   $$ |$$/   _______  _$$ |_   \n /      \\ /  |$$ |_ $$// $$   |  $$ |/  | /       |/ $$   |  \n/$$$$$$  |$$ |$$   |   $$$$$$/   $$ |$$ |/$$$$$$$/ $$$$$$/   \n$$ |  $$ |$$ |$$$$/      $$ | __ $$ |$$ |$$      \\   $$ | __ \n$$ \\__$$ |$$ |$$ |       $$ |/  |$$ |$$ | $$$$$$  |  $$ |/  |\n$$    $$ |$$ |$$ |       $$  $$/ $$ |$$ |/     $$/   $$  $$/ \n $$$$$$$ |$$/ $$/         $$$$/  $$/ $$/ $$$$$$$/     $$$$/  \n/  \\__$$ |                                                   \n$$    $$/                                                    \n $$$$$$/                                                     \n\n");
    printf("We have a variety of awsesome gifts:\n1) Ploy Stetion 5.\n2) SuperPasqal1.\n3) Xknox.\n4) More pop ups.\n\n");


    wlist.size = 0;
    while (wlist.size==0 || wlist.size>4){
        printf("Enter the size of your wish list > ");
        scanf("%d", &wlist.size);
        fflush(stdin);
    }

    for (index = 0; index < wlist.size; index++){
        wlist.list[index] = 0;
    }

    while (1){
        printf("\n1) Print gift list.\n2) Edit a slot.\n3) Print wish list.\n4) Message from the admin.\n5) Quit\n\nInsert your choice > ");
        scanf("%d", &menu_choice);
        fflush(stdin);
        switch (menu_choice)
            {
            case 1:
                printf("\nOur awesome gifts:\n1) Ploy Stetion 5.\n2) SuperPasqal1.\n3) Xknox.\n4) More pop ups.\n\n");
                break;
            case 2:
                index = wlist.size+1;
                while (index<0 || index>wlist.size){
                    printf("Slot to fill > ");
                    scanf("%d", &index);
                    fflush(stdin);
                }
                gift = 6;
                while (gift>5){
                    printf("Gift number > ");
                    scanf("%d", &gift);
                    fflush(stdin);
                }
                wlist.list[index-1] = gift;
            case 3:
                print_wlist(wlist);
                break;
            case 4:
                if (!wlist.admin){
                    printf("Only the admin can leave a message.\n");
                }else{
                    admin_message();
                }
                break;
            default:
                printf("\nYour gifts are on the way!\n");
                return 0;
                break;
            }
    }

    return 0;
}