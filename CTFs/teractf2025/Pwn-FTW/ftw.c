#include <stdio.h>
#include <stdlib.h>

// gcc ftw.c -o ftw -fno-stack-protector  -no-pie -m32

FILE *fptr;
char daflag[32]; 

void win(long first, long second) {
   fptr = fopen("./flag.txt", "r");
   if (fptr == NULL) {
	printf("No flag.txt file found\n");
	fflush(stdout);
	exit(1);
   }
   fgets(daflag, 32, fptr);
   printf("Wow! Have a flag: %s\n\n", daflag);
   fflush(stdout);
}

void whodis() {
    char buffer[32];

    printf("Enter your name: ");
    fflush(stdout);
    scanf("%s", buffer);
    printf("\nI don't know you, %s. Cya!\n", buffer);    
}

int main() {
    whodis();
    return 0;
}
