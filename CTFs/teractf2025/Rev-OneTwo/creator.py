#!/usr/bin/env python3

flag = "teractf{1t5_ju5t_l1k3_march31ng_l3ft_r1ght!}"
half_flag = len(flag) // 2
mixed_flag = ""
for i in range(half_flag):
  mixed_flag += flag[i]+flag[i + half_flag]

print(mixed_flag)
