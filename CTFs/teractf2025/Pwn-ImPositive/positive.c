#include <stdio.h>
#include <stdlib.h>

int x, y, z;
FILE *flag_ptr;
char flag[40];

int intro() {
	printf("\tI'm positive you'll like my number adder!\n");
	printf("\tSupply two integers separate by a space and I'll do the rest\n");
	printf("\tDon't try to use any negative numbers!  We need to stay positive!\n\n");
	fflush(stdout);
	return 0;
}

int maths() {
	printf("Enter a positive integer: ");
	fflush(stdout);
	scanf("%d", &x);
	printf("Enter another positive integer: ");
	fflush(stdout);
	scanf("%d", &y);
	if (x < 1 || y < 1){
		printf("\nNice try!  I said 'Be Positive!'\n\n");
		fflush(stdout);
		return 1;
	}	
	z = x + y;
	if (z <= 0) {
		printf("\nWhat..What...What?!? Oh well, maybe a flag will make you positive\n\t");
		fflush(stdout);
		flag_ptr = fopen("./flag.txt", "r"); 
		if (flag_ptr != NULL){
			while (fgets(flag, 40, flag_ptr)) {
				printf("%s", flag);
				fflush(stdout);
			};
			fclose(flag_ptr);
			printf("\n");
			fflush(stdout);
			
		}
		else {
			printf("Something's gone seriously wrong, open a ticket\n\n");
			fflush(stdout);
		}
		return 0;
	}
	else {
		printf("\nYour total is %d, but that's not positive enough\n\n", z);
		fflush(stdout);
		return 1;
	}
}

int main(){
	intro();
	maths();
	exit(0);
}
