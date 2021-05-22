#include <stdio.h>
#include <stdlib.h>


void get_flag(){
	int fd;
	char flag[180];
	fd = fopen("./flag","r");
	fscanf(fd,"%s",flag);
	printf("Plz have the flag: %s\n",flag);
	fclose(fd);
}

void access_granted(){
	printf("**************************\n");
	printf("***   ACCESS GRANTED   ***\n");
	printf("**************************\n");
	fflush(stdout);
}

void access_denied(){
	printf("**************************\n");
	printf("***   ACCESS DENIED    ***\n");
	printf("**************************\n");
	fflush(stdout);
}

void check_passwd(){
	int fd;
	char password[180];
	char real_passwd[180];
	printf("Please input correct password to get access!\n");
	fflush(stdout);
	gets(password);
	fd = fopen("./flag","r");
	fscanf(fd,"%s", real_passwd);
	fclose(fd);
	if(!strcmp(password,real_passwd)){
		access_granted();
	}
	else{
		access_denied();
	}
}

int main(){
	printf("Welcome to super secure password checker!\n");
	check_passwd();
	return 0;
}
