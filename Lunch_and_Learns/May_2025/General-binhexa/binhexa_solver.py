#!/usr/bin/env python3

from pwn import *

p = remote("titan.picoctf.net", 52076)
#context.log_level = "DEBUG"

p.readuntil(b'1: ')
v1 = int(p.readline().decode().strip(), 2)
p.readuntil(b'2: ')
v2 = int(p.readline().decode().strip(), 2)

bin_nums = [ v1, v2]
ans = 0
for _ in range(6):
    p.readuntil(b"Operation")
    op = p.readline().decode().split(':')[1].strip()
    match op:
        case "'<<'":
            p.readuntil(b'Number ')
            num = int(p.readline().decode().split()[0].strip()) - 1
            ans = bin_nums[num] << 1
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())
        case "'>>'":
            p.readuntil(b'Number ')
            num = int(p.readline().decode().split()[0].strip()) - 1
            ans = bin_nums[num] >> 1
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())
        case "'|'":
            ans = bin_nums[0] | bin_nums[1]
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())
        case "'&'":
            ans = bin_nums[0] & bin_nums[1]
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())
        case "'+'":
            ans = bin_nums[0] + bin_nums[1]
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())
        case "'*'":
            ans = bin_nums[0] * bin_nums[1]
            p.readuntil(b'result: ')
            p.sendline(f'{ans:b}'.encode())

p.recvuntil(b'hexadecimal: ')
p.sendline(f'{ans:x}'.encode())
p.recvuntil(b'flag is:')
print(p.recvline().decode().strip())

