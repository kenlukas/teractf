# Chronohack

## Reverse

### Can you guess the exact token and unlock the hidden flag?  Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important file for token generation. Guess the token to get the flag.

The token_generation.py contains:

```python
import random
import time

def get_random(length):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(int(time.time() * 1000))  # seeding with current time 
    print(f'script time: {time.time()*1000}')
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def flag():
    with open('flag.txt', 'r') as picoCTF:
        content = picoCTF.read()
        print(content)


def main():
    print("Welcome to the token generation challenge!")
    print("Can you guess the token?")
    token_length = 20  # the token length
    token = get_random(token_length) 
    print(f'{token = }')

    try:
        n=0
        while n < 50:
            user_guess = input("\nEnter your guess for the token (or exit):").strip()
            n+=1
            if user_guess == "exit":
                print("Exiting the program...")
                break
            
            if user_guess == token:
                print("Congratulations! You found the correct token.")
                flag()
                break
            else:
                print("Sorry, your token does not match. Try again!")
            if n == 50:
                print("\nYou exhausted your attempts, Bye!")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting the program...")

if __name__ == "__main__":
    main()
```

The first thing I do is review the code.  This sets the length of the token to guess at 20.  Then it creates random token each time the script is run.
Next it sets up a `try` condition that breaks out of the loop if you hit Ctrl-C.  It then sets up a loop with a counter (n) that is set to 50.
Then you can enter your guess at the token.  If you input the token, you get the flag.  Otherwise it will continue to ask until you reach the limit and it ends.  Simple enough.

Next, I evaluate the functions it's calling.  In this case, I'm mostly interested in the `get_random` function that returns the token.  The first line sets the variable it will use to pick characters for the token from.  For this program, it's using digits, and upper and lowercase letters.  The next line creates a randomization seed.

I interrupt this walkthrough to bring you this important message:

Computers suck at random!  Computers are predictable.  You put x in, you'll get y out.  This is good and bad.  It's great for creating repeatable processes.  It's horrible for encryption.  There are two methods of encryption a computer uses.  PRNGs are pseudo-random number generators.  The keyword is "pseudo"!  The algorithm it uses relies on a `seed`.  The seed is a starting point.  It tells the randomization function to start your random number generation at X.  The problem is, if I know X, I can get the same "random" output again.

For example, if I set a seed value to say 100, and use the lowercase alphabet to make random selections:

```python
import random
random.seed(100)
alphabet = "abcdefghijklmnopqrstuvwxyz"

for _ in range(3):
    print(random(choice(alphabet)))
```
This will randomly choose: 'eoo', and if I reset the seed, and run the program again I'll get the same output.  Not so random.

I now return you to your regularly scheduled walkthrough....

The seed is being set to the current time the program is run times 1000.

I interrupt this walkthrough to bring you another important message:

Unix keeps time in incrementing a number each second beginning on 1 January 1970.  This is known as epoch time.  If you print the current time using the `time` function in Python you'll get a number like: 1744980437411.6597.  This number not only includes the number of seconds since the epoch, it also includes milliseconds.  Everything after the decimal point is nanoseconds.

I now return you to the original walkthrough....

When the time is multiplied we now get a time that includes nanoseconds.  This makes figuring out the seed value even harder, but not impossible.  Because the program is giving us 50 tries we have some leeway to guess the seed, but we'll never be able to do it by hand.  We need automation.

Python and pwntools to the rescue!




```python
#!/usr/bin/env python3

import time
import random
from pwn import *

#context.log_level = "DEBUG"
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#  Mirror the token generation from the script
def my_token(time_now):
    random.seed(time_now)
    token = ""
    for i in range(20):
        token += random.choice(alphabet)
    return token
# Loop until we find the flag. The counter isn't really necessary but the 
#   error message we get after we hit the 50 try limit is ugly
not_found = True
counter = 0
# When doing it locally we don't need to add any time, but remotely there's a lag
lag = 120
# Get our current time, before starting the program
time_now = int(time.time() * 1000 + lag )
# This starts the process locally or remotely - since it started after we got the time we'll be behind
#p = process(['python3', 'token_generator.py']) 
p = remote('verbal-sleep.picoctf.net', 63905)

# Send our token guess, check if we got it right, and if not, add one to time_now and repeat
#  This happens very fast, so we will catch up to the applications recorded time pretty quickly
while not_found:
    p.sendlineafter(b'exit):', my_token(time_now).encode())
    resp = p.recvline().decode().strip()
    if 'Congratulations' in resp:
        flag = p.recvline()
        print(f'{flag}')
        not_found = False
    time_now += 1
    counter += 1
    if counter == 50:
        not_found = False
        print(f'Ran out of time')

```

**picoCTF{UseSecure#$_Random@j3n3r@T0rsde389b79}**
