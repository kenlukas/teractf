#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  char flag[64];
  char *flag_ptr = flag;

  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("I'm testing a proof of concept.  You won't overflow the buffer.  This program will repeat whatever you input");

  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Where's the flag.txt file?\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);

  while(1) {
    printf(": ");
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }
  return 0;
}
