#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

FILE *flag_ptr;
char buffer[50];

void get_flag(char *buffer){
	flag_ptr = fopen("flag.txt", "r");
	fgets(buffer, 50, flag_ptr);
}

char *sha256(char *input) {
  unsigned char hash[SHA256_DIGEST_LENGTH];
  SHA256_CTX ctx;

  SHA256_Init(&ctx);
  SHA256_Update(&ctx, input, strlen(input));
  SHA256_Final(hash, &ctx);

  char *output = malloc(SHA256_DIGEST_LENGTH * 2 + 1);
  if (output == NULL) {
	  printf("\nMemory Allocation Error\n");
	  exit(1);
  }
  for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
    snprintf(output + i * 2, 3, "%02x", hash[i]);
  }
  return output;
}


void menu(){
	printf("1) Please print the hash of the flag\n2) I want to guess\n3) exit\n\n");
	printf("Make a selection: ");
	fflush(stdout);
}

int read_input(){
	char input;
	input = getchar();
	fflush(stdin);
	return atoi(&input);
}

int check_hash(char *hash_str, char *usr_str){
	char *flag_hash = sha256(hash_str);
	char *user_hash = sha256(usr_str);
	return strncmp(flag_hash, user_hash, 6);
}


void output_flag(){}

int main() {
	int ans = 0;
	printf("\nWelcome! If you ask nicely, I'll give you the sha256 hash of the flag.\n");
	printf("and if you give me a string whose sha256 hash collides with the first six \ncharacters of the flags hash, I'll give you the unhashed version\n\n");
	fflush(stdout);
	get_flag(buffer);
	char *my_hash = sha256(buffer);
	char resp[30];
	while(1) {
		menu();
		ans = read_input();
		switch (ans) {
			case 1:
				printf("\nThe hashed flag is: %s\n", my_hash);
				fflush(stdout);
				break;
			case 2:
				printf("Cool!  Give me your string and I'll check it: ");
				fflush(stdout);
				int c;
				while ( (c = getchar()) != EOF && c != '\n') {}
				if (fgets(resp, sizeof(resp), stdin) != NULL) {
					size_t len = strlen(resp);
					if (len > 0 && resp[len - 1] == '\n') {
						resp[len - 1] = '\0';
					}
				} else {
					printf("\nWTF is going on???\n");
					exit(1);
				}
				if (! (strncmp(sha256(buffer),sha256(resp), 6))) {
					printf("\nYes!  That's a mini collision\nHere's the flag: %s\n", buffer);
				} else {
					printf("\nNope!  Better luck next time!\n");
				}
				break;
			case 3:
				return 0;
		}
		return 0;
	}
	fclose(flag_ptr);
	free(my_hash);

	return 0;
}


