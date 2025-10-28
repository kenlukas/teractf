#!/usr/bin/env python3

enc_flag = "5463525F61546659877D685F54117D5568116E7D54681152117D5F52117D6B536C5487506C117D66536E615487106E7D615F6C6C135B4A"
flag = ""

for i in range(0, len(enc_flag), 2):
  my_num = int(enc_flag[i:i+2], 16)
  flag += chr((my_num - 0xf) ^ 0x31)

print(flag)
