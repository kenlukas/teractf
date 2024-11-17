#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  char passwd[25];
  FILE *fp;
  char flag[40];

  printf("Enter the password: ");
  fgets(passwd, sizeof(passwd), stdin);
  passwd[strlen(passwd)-1] = '\0';

  if (strcmp(passwd, "all-american-rejects") == 0) {
	  fp = fopen("flag.txt", "r");
	  if (fp) {
		  fscanf(fp, "%[^\n]", flag);
	  	  printf("You Rock!  Have a flag: %s\n", flag);
	  } 
	  else {
		  printf("WTF?  There's no flag!?!");
		  exit(1);
	  }

  }
  else {
	  printf("Nah, that's not it, see ya!\n");
  }
  return 0;
}
