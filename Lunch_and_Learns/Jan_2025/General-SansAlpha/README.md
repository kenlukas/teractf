# SansAlpha

## General

### The Multiverse is within your grasp! Unfortunately, the server that contains the secrets of the multiverse is in a universe where keyboards only have numbers and (most) symbols.  Additional details will be available after launching your challenge instance.

```sh
$ ssh -p 60638 ctf-player@mimas.picoctf.net
The authenticity of host '[mimas.picoctf.net]:60638 ([52.15.88.75]:60638)' can't be established.
ED25519 key fingerprint is SHA256:n/hDgUtuTTF85Id7k2fxmHvb6rrLrACHNM6xLZ46AqQ.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:3: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[mimas.picoctf.net]:60638' (ED25519) to the list of known hosts.
ctf-player@mimas.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1016-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

SansAlpha$ ls
SansAlpha: Unknown character detected
SansAlpha$ pwd
SansAlpha: Unknown character detected
SansAlpha$ 1
bash: 1: command not found

# * will try to run the first command alphabetically in the current directory
SansAlpha$ *
bash: blargh: command not found

# by adding the / it's still trying to run the first command but the slash makes it see blargh as a directory
SansAlpha$ */
bash: blargh/: Is a directory

# Let's see what's in the blargh directory
SansAlpha$ */*
bash: blargh/flag.txt: Permission denied

# Okay, we know where the flag is.  What's in the directory above blargh
SansAlpha$ ../*
bash: ../ctf-player: Is a directory

# Another directory, and this one gives us letters we can use to our advantage

SansAlpha$ ${_:3:1}
bash: c: command not found

# By using the ${} parameter notation, we can take the output from the previous command and print the 4th (index 3) letter

SansAlpha$ ../*
bash: ../ctf-player: Is a directory

#  To cat the flag, put a few parameters together

SansAlpha$ ${_:3:1}${_:9:1}${_:4:1} */*
return 0 picoCTF{7h15_mu171v3r53_15_m4dn355_640b6add}Alpha-9, a distinctive layer within the Calastran multiverse, stands as a
sanctuary realm offering individuals a rare opportunity for rebirth and
introspection. Positioned as a serene refuge between the higher and lower
Layers, Alpha-9 serves as a cosmic haven where beings can start anew,
unburdened by the complexities of their past lives. The realm is characterized
by ethereal landscapes and soothing energies that facilitate healing and
self-discovery. Quantum Resonance Wells, unique to Alpha-9, act as conduits for
individuals to reflect on their past experiences from a safe and contemplative
distance. Here, time flows differently, providing a respite for those seeking
solace and renewal. Residents of Alpha-9 find themselves surrounded by an
atmosphere of rejuvenation, encouraging personal growth and the exploration of
untapped potential. While the layer offers a haven for introspection, it is not
without its challenges, as individuals must confront their past and navigate
the delicate equilibrium between redemption and self-acceptance within this
tranquil cosmic retreat.

SansAlpha$  
```
:joy:

**picoCTF{7h15_mu171v3r53_15_m4dn355_640b6add}**
