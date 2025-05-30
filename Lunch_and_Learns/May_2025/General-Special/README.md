# Special

## General

### Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)

This one was a bit of a pain.  The block belows shows some of the attempts that I made and the results.  I eventually figured out a method to get the flag using pipes, but I wasn't sure it was the way the challenge author had intended.  All in all this took me about 20 minutes to get this answer.  Below that is what I think the author had intended.

```sh
Special$ ls
Is 
sh: 1: Is: not found
Special$ whoami
Whom 
sh: 1: Whom: not found
Special$ pwd
Pod 
sh: 1: Pod: not found
Special$ ls|ls
Lulls 
sh: 1: Lulls: not found
Special$ pwd|ls
Pedals 
sh: 1: Pedals: not found
Special$ pwd|cat *
Pwd|cat * 
sh: 1: Pwd: not found
cat: blargh: Is a directory
Special$ pwd|cat blargh/*
Pwd|cat blargh/* 
sh: 1: Pwd: not found
picoCTF{5p311ch3ck_15_7h3_w0r57_f906e25a}Special$
```

This is a bit more elegant:

```sh
Special$ ${parameter=cat blargh/flag.txt}
${parameter=cat blargh/flag.txt} 
picoCTF{5p311ch3ck_15_7h3_w0r57_f906e25a}Special$ 
```

**picoCTF{5p311ch3ck_15_7h3_w0r57_f906e25a}**
