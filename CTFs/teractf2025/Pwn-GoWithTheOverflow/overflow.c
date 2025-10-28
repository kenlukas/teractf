#include <stdio.h>
#include <stdlib.h>

#pragma GCC diagnostic ignored "-Wimplicit-function-declaration"

char buffer[30];
int blah;
FILE *fptr;
char daflag[50];

int main() {
	blah = 1337;
	printf("\n\nAre you able to go with the (over) flow?\n");
	printf("What's your favorite word? ");
	fflush(stdout);
	gets(buffer);
	if (blah == 1337){
		printf("\nYou didn't get into the flow\n");
		fflush(stdout);
	}else{
		printf("\nNice job, going with the flow\n");
		fptr = fopen("./flag.txt", "r");
		fgets(daflag, 46, fptr);
		fclose(fptr);
		printf("Let your flag flow: %s\n\n", daflag);
		fflush(stdout);
	}
	return 0;
}

