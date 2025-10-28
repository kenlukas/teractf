# MyCrypto

## Rev

### Cryptography is easy, all you need to do is XOR to values with a special key.  So easy.

> This is the encoded flag (hex): b'23181e4216270a2c420b5d3f3a64121013631b43233e1e74181741150f62413467281e44663e0d711362235b'

```python
#!/usr/bin/env python3
import random
import string
from binascii import hexlify, unhexlify


chars = string.ascii_letters + string.digits
# MyCrypto
key = ''.join(random.choice(chars) for _ in range(4))

with open("./flag.txt", "r") as f: flag = f.read()

def encode_str(flag_str: str, key: str) -> bytes:
  flag_bytes = flag_str.encode()
  key_bytes = key.encode()
  result_bytes = bytes( ((d ^ key_bytes[i%4]) + 9) for i, d in enumerate(flag_bytes))
  return result_bytes

output = encode_str(flag, key)
print(f'encoded flag (hex): {hexlify(output)}')
```

Okay, we're given the encoded flag and the program that was used to create it.  The key is a combination of four random letters (upper and lowercase), or numbers.  The flag is encoded by xor'ing the flag with a character from the key and then 9 is added to it.

Since the flag is only four characters, and we know the flag starts with `teractf{` we can reverse the encoded flag to get the key and test it against the 5-8 bytes in the encoded flag.

For example we know the first character of the flag is a `t`, we can subtract 9 from the first byte in the encoded flag and xor it with `t` to get the first value of the flag (110 which is the letter `n`).  We can then text it on the fifth byte in the flag (0x16) to see if we get the expected value (c). This works:

```python
>>> (0x23-9) ^ ord('t')
110
>>> (0x16-9) ^ 110
99
>>> chr(99)
'c'
>>> (0x23-9) ^ 110
116
>>> chr(116)
't'
```
We could do this for all manually but it's easier to write a script.


**teractf{Wh3n_1n_d0ubt_r3ad_Th3_s0urc3_c0d3}**
