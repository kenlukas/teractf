#include <stdio.h>
#include <unistd.h>

char flag[40] = "teractf{1t_a1nt_n0_l13_84by_8y3_8y3_8y3}";

int main() {
	sleep(1);
	printf("It might sound crazy ");
	fflush(stdout);
	for (int i = 0;i < 3; i++) {
	    sleep(1);
	    printf(".");
	    fflush(stdout);
	}
	printf("\n\tbut it ain't no lie ");
	fflush(stdout);
	for (int i = 0;i < 3; i++) {
	    sleep(1);
	    printf(".");
	    fflush(stdout);
	}
	printf("\n\t\tBaby\n");
	sleep(1);
	printf("\t\t\tBye\n");
	sleep(1);
	printf("\t\t\t\tBye\n");
	sleep(1);
	printf("\t\t\t\t\tBye!\n");
	return 0;
}
