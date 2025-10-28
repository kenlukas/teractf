# One Two

## Reverse Engineering

### I don't know what to make of this.  I'm sure there's a flag in there somewhere.  tmearraccht3f1{n1gt_5l_3jfut5_tr_1lg1hkt3!_}

If you look closely you can see that every other letter would be the start of a string.

I wrote the following script to unshuffle them:

```python
#!/usr/bin/env python3

jumble = "tmearraccht3f1{n1gt_5l_3jfut5_tr_1lg1hkt3!_}"
left = ""
right = ""

for i in range(0, len(jumble), 2):
  left += jumble[i]
  right += jumble[i+1]

print(f'{left}{right}')
```



**teractf{1t5_ju5t_l1k3_march31ng_l3ft_r1ght!}**
