#include <stdio.h>

// gcc youdontownme.c -o youdontownme -fno-stack-protector  -no-pie -m32

FILE *fptr;
char daflag[32]; 

void win(long first, long second) {
    if (first == 0xdeadbeef && second == 0xc0defeed){
        fptr = fopen("./flag.txt", "r");
	if (file == NULL) {
		printf("No flag.txt file found\n");
		return 1;
	fgets(daflag, 32, fptr);
	printf("Wow! You do own me!  Have a Flag\n%s\n", daflag);
    }else{
        printf("You Don't Own Me, So Don't Tell Me What To Do!!\n");
    }
    fflush(stdout);
}

void whodis() {
    char buffer[32];

    printf("Enter your name: ");
    fflush(stdout);
    scanf("%s", buffer);
    printf("\nI don't know you, %s. Goodbye!\n", buffer);    
}

int main() {
    whodis();
    return 0;
}
