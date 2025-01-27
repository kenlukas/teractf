from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Binary filename
exe = './maths'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
#context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================
io = start()

for i in range(2000):
   question =  io.recvuntil(b'?')
   q = question.decode('utf-8').split()
   if '+' in q:
       x, y = int(q[2]),int(q[4])
       ans = str(x + y)
   elif '-' in q:
       x, y = int(q[2]),int(q[4])
       ans = str(x - y)
   elif 'squared?' in q:
       x = int(q[2])
       ans = str(x**2)
   elif '*' in q:
       x,y = int(q[2]), int(q[4])
       ans = str(x * y)
   else:
       print(f"WTF??")
       exit()
   io.sendline(ans)
       

# Receive the flag
io.interactive()
