import time
import random

questions = int(input("How many questions do you want to answer? "))

for i in range(questions):
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    ans = int(input(f"What is {a} + {b} = "))

    print("calculating")

    totaltime = pow(2, i)

    print('...')
    time.sleep(totaltime / 3)
    print('...')
    time.sleep(totaltime / 3)
    print('...')
    time.sleep(totaltime / 3)

    if ans != a + b:
        print(f"I weep for the future 😭")
        exit(69)

f = open('./flag.txt', 'r')
flag = f.read()
print(flag[:questions])
