# Binary Search

## General

### Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.  Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

This challenge is pretty straightforward.  I downloaded the challenge from the site, created an automated solver, and hit a wall when I realized the challenge uses ssh for access without a command prompt.  This should be automatible using Python and pexpect but I ran out of time to construct it. 

```sh
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Lower! Try again.
Enter your guess: 125
Higher! Try again.
Enter your guess: 188
Lower! Try again.
Enter your guess: 157
Lower! Try again.
Enter your guess: 141
Higher! Try again.
Enter your guess: 149
Higher! Try again.
Enter your guess: 153
Higher! Try again.
Enter your guess: 155
Congratulations! You guessed the correct number: 155
Here's your flag: picoCTF{g00d_gu355_2e90d29b}
Connection to atlas.picoctf.net closed.
```

**picoCTF{g00d_gu355_2e90d29b}**
