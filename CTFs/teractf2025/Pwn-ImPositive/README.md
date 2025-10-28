# I'm Positive

## Pwn

### I'm positive you'll like this challenge!  Don't bring those negative vibes here.

This challenge came with C source code and a binary.

Source
```C
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
```

From reading the source code, the code will only accept positive integers as input.  It then adds up, and if the result is positive, it shows the result, BUT if it's negative, it gives the flag!  This is an integer overflow vulnerability.

The integers in this code are signed integers. What that means is it can be a positive or negative (or zero) value.  How it does this can be a bit (pun intended) strange at first.  If you already know this, skip ahead to the solution.  An integer is usually 32 bits in C.  That means there are 32 1's or 0's that represent a number in binary.  For a signed integer, the right-most 31 bits are positive until the 32nd bit (furthest left) is 1; then all values are negative.  The top answer [here](https://stackoverflow.com/questions/5739888/what-is-the-difference-between-signed-and-unsigned-int) gives a good visual representation of what I'm talking about using a 4-bit number as an example. Long story longer... If you assign a value to a signed integer larger than the maximum positive value (2147483647), it will be interpreted as a negative number by the program.

**Solution:**
Since it checks each integer after input, you need to use a value for one that is the maximum (or almost the maximum), and a second number that, when added to it, will overflow the signed integer, making it negative.  The program then interprets the addend as a negative number and gives the flag.


```sh
$ nc localhost 2227
	I'm positive you'll like my number adder!
	Supply two integers separate by a space and I'll do the rest
	Don't try to use any negative numbers!  We need to stay positive!

Enter a positive integer: 2147483646
Enter another positive integer: 4

What..What...What?!? Oh well, maybe a flag will make you positive
	teractf{1m_p0sitiv3_y0u_w3r3_n3gativ3}
```

**teractf{1m_p0sitiv3_y0u_w3r3_n3gativ3}**
