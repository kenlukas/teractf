#!/usr/bin/env python3

import random
from datetime import datetime
import time

random.seed(int(datetime.now().timestamp()))
i = 0
while i <= 2000:
    # print(f"random is {random.randint(1,4)}")
    x = random.randint(0,9)
    y = random.randint(0,9)
    func = random.randint(1,4)
    start = datetime.now().timestamp()
    if func == 1:
        print(f"What is {x} + {y} ? ", end="")
        ans = x + y
    elif func == 2:
        if x < y:
            x, y = y, x
        print(f"What is {x} - {y} ? ", end="")
        ans = x - y
    elif func == 3:
        print(f"What is {x} x {y} ? ", end="")
        ans = x * y
    else:
        print(f"What is {x} squared ? ", end="")
        ans = x ** 2

    i = i + 1 

    if ans != int(input("")):
        print(f"Common man, we're outta here")
        exit(1)
    elif datetime.now().timestamp() - start > 3:
        print(f"Ah man, you ran out of time")
        exit(2)
    
print("Heck yeah!  Have a flag!: ", end="")

#for i in range(50):
#    print(f'this is randint: {random.randint(1,4)}')
