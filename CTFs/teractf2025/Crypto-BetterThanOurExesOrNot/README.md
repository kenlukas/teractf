# Better Than Our eXes OR Not

## Cryptography

### Xor is for the meek!  To really eXcel you need to XNOR!  The all or nothing gate!

This challenge comes with two files, one is the Python code used to encrypt the flag and the other one showing the output.

First the output shows when a static string is encoded, and the second gives the encrypted flag.
 
xnor_out.txt

```sh
Key: [REDACTED]

Message: b'When is it safe to use the same key??'
Encrypted message: df06bc4814d511416ea69b4a7a7238f3dd9de891a5254bdb84499dc22ead6d9fcb94da9ed8

Flag: [REDACTED]
Encrypted flag: fc0bab4757c8041a70e1e458692702e3d982f897bf34589ab31cdbee7fb57ae0938990949a
```

xnor.py
```python
import os


def xnor_bit(a_bit, b_bit):
    if a_bit == "1" and b_bit == "1":
        return "1"
    elif a_bit == "1" and b_bit == "0":
        return "0"
    elif a_bit == "0" and b_bit == "1":
        return "0"
    elif a_bit == "0" and b_bit == "0":
        return "1"


def xnor_byte(a_byte, b_byte):
    a_bits = get_bits_from_byte(a_byte)
    b_bits = get_bits_from_byte(b_byte)

    result_bits = [xnor_bit(a_bits[i], b_bits[i]) for i in range(8)]
    result_byte = get_byte_from_bits(result_bits)
    return result_byte


def xnor_bytes(a_bytes, b_bytes):
    assert len(a_bytes) == len(b_bytes)

    return bytes([xnor_byte(a_bytes[i], b_bytes[i]) for i in range(len(a_bytes))])


def get_bits_from_byte(byte):
    return list("{:08b}".format(byte))


def get_byte_from_bits(bits):
    return int("".join(bits), 2)


message = b"When is it safe to use the same key??"
key = os.urandom(37)
# Fake Flag for Testing
flag = b'teractf{need_a_37_char_string_4_test}'


def main():
    print(f"Key: {key.hex()}")
    print(f"\nMessage: {message}")

    encrypted = xnor_bytes(message, key)
    print(f"Encrypted message: {encrypted.hex()}")

    print(f"\nFlag: {flag}")
    encrypted_flag = xnor_bytes(flag, key)
    print(f"Encrypted flag: {encrypted_flag.hex()}")


if __name__ == "__main__":
    main()
```

Authors Note:  I wanted this to be a lot harder but in this case, math made it easier.
```sh
XNOR=¬(XOR)
From A XNOR B=C, you get B=A⊕¬C
But XOR and XNOR are both self-inverse, so:
  A XNOR B=C
  A⊕C=B′ (the bitwise complement of the true key)
  Complementing again gives the true key
```
In this case, you know A (the static string characters) and you know ¬C because that's the encrypted value.  XOR'ing them give B which is the key.

Here's the code I used to solve it:

```python
#!/usr/bin/env python3

static_str = "When is it safe to use the same key??"
static_enc = "df06bc4814d511416ea69b4a7a7238f3dd9de891a5254bdb84499dc22ead6d9fcb94da9ed8"
flag_enc = "fc0bab4757c8041a70e1e458692702e3d982f897bf34589ab31cdbee7fb57ae0938990949a"
flag = ""

for i in range(len(static_str)):
  j = i * 2
  key = ord(static_str[i]) ^ int(static_enc[j:j+2], 16)
  flag += chr(key ^ int(flag_enc[j:j+2], 16))

print(flag)
```

**teractf{w3_ar3_0pp0sit35_0f_0ur_3x35}**
