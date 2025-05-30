# Specialer

## General

### Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.

I had the benefit of experience for this challenge.  The UNIX `echo` command is used a lot in CTFs.  After trying a few different commands, I found `echo` was available.  We used a glob `*` in one of the first Lunch and Learns.  In this case we're using it to echo the contents of a directory since `ls` isn't available.  

The key to this is being able to send the contents of a file to the echo command.  Using `$(<file.txt)` syntax is effectively doing the same thing as `cat file.txt`.  It's actually more efficient because it doesn't create a subprocess.  To break it down `$(----)` runs the commands within the parentheses and the outputs the output of the command.  The `<file.txt` uses the input redirection to pipe stdin, effectively sending the contents of file.txt to stdin.

```sh
Specialer$ ls
-bash: ls: command not found
Specialer$ pwd
/home/ctf-player
Specialer$ whoami
-bash: whoami: command not found
Specialer$ w
-bash: w: command not found
Specialer$ cat cat
-bash: cat: command not found
Specialer$ echo 'blah'
blah
Specialer$ echo *
abra ala sim
Specialer$ echo abra/*
abra/cadabra.txt abra/cadaniel.txt
Specialer$ echo abra/cadabra.txt
abra/cadabra.txt
Specialer$ echo abra/cadabra*   
abra/cadabra.txt
Specialer$ echo "$(<abra/cadabra.txt)"
Nothing up my sleeve!
Specialer$ echo "$(<abra/cadaniel.txt)"
Yes, I did it! I really did it! I'm a true wizard!
Specialer$ echo ala/*        
ala/kazam.txt ala/mode.txt
Specialer$ echo "$(<ala/kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}
```

**picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}**
