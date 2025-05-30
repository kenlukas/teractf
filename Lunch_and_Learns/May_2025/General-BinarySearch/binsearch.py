#!/usr/bin/env python3
###############################################################################################
# This solves the Binary Search challenge on picoCTF, successful guessing will reveal the flag
# Parameters (order specific) : <port> <password>
# Output: Program results
#
# Note: you may need to change the domain name
###############################################################################################

import pexpect
import sys

port = int(sys.argv[1])
password = sys.argv[2]
high = 1000
low = 1
last = 500
child = pexpect.spawn(f'ssh -p {port} ctf-player@atlas.picoctf.net')
#child.expect('Are you sure.*')
#child.sendline('yes')
child.expect('password:')
child.sendline(password)
child.expect('guess: ')
child.sendline(str(last))
for _ in range(10):
    outcome = child.expect(['Higher! Try again.', 'Lower! Try again', 'Congratulations', 'Sorry'])
    if outcome == 0:
        low = last
    elif outcome == 1:
        high = last
    elif outcome == 2:
        break
    else:
        break
    last = (high + low) // 2
    child.expect('guess: ')
    child.sendline(str(last))


child.interact()

