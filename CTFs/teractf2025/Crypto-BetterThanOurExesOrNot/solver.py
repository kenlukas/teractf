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

