#!/usr/bin/env python3

jumble = "tmearraccht3f1{n1gt_5l_3jfut5_tr_1lg1hkt3!_}"
left = ""
right = ""

for i in range(0, len(jumble), 2):
  left += jumble[i]
  right += jumble[i+1]

print(f'{left}{right}')
