#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int LOOP_CNT = 2;

int i, rand_num, the_ans, ans = 0;
int x;
int y;
time_t start, finish;
FILE *fp;


int main(){
  while (i < LOOP_CNT) {
	  int tmp = 0;
          srand(time(NULL));
          x = rand() % 9 + 1;
          y = rand() % 9 + 1;
          rand_num = rand() % 4 + 1; 
          time(&start); 
    if (rand_num == 1) {
            printf("What is %d + %d ? ", x, y);
            ans = x + y;
    } else if (rand_num == 2){
	    if (x < y) {
		    tmp = x;
		    x = y;
		    y = tmp;
            }
	    printf("What is %d - %d ? ", x, y);
	    ans = x - y;
    } else if (rand_num == 3) {
	    printf("What is %d * %d ? ", x, y);
	    ans = x * y;
    } else {
	    printf("What is %d squared? ", x);
	    ans = x * x;
    }
    fflush(stdout);
    i++;
    scanf("%d", &the_ans); 
    time(&finish);
    if (ans != the_ans){
	    printf("\nC'mon man, we're outta here!\n");
	    exit(1);
    } else if (difftime(finish, start) > 3) {
	    printf("\nAwww man, you ran out of time\n");
	    exit(2);
    }
    fflush(stdout);
  }
fp = fopen("./flag.txt", "r");

if (fp == NULL) {
	printf("\nYou need to put a dummy flag.txt file\n");
	exit(3);
}

char ch;
printf("\nHell yeah!  You're a Math-lete!  Have a flag: ");
while ((ch = fgetc(fp)) != EOF) {
	printf("%c", ch);
}

printf("\n\n");
fclose(fp);

}


