#!/usr/bin/env python3
import random
import string
from binascii import hexlify, unhexlify


chars = string.ascii_letters + string.digits
key = ''.join(random.choice(chars) for _ in range(4))

with open("./flag.txt", "r") as f: flag = f.read()

def encode_str(flag_str: str, key: str) -> bytes:
  flag_bytes = flag_str.encode()
  key_bytes = key.encode()
  result_bytes = bytes( ((d ^ key_bytes[i%4]) + 9) for i, d in enumerate(flag_bytes))
  return result_bytes

output = encode_str(flag, key)
print(f'encoded flag (hex): {hexlify(output)}')

