# Wave a Flag

## General

### Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

I believe the intended way to solve this is to give the program executable permissions and run it:

```sh
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b11c22752c901adc13ba1ce86eda9d5516f22763, with debug_info, not stripped

$ chmod 755 warm
$ ./warm
Hello user! Pass me a -h to learn what I can do!
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_d6969390}
```
But there are other ways to solve it.  Unix has a `strings` command that outputs printable characters from a file.  This is extremely useful for finding plain text in a binary file.

If you run `strings warm` you'll get the printable text in the file output to the screen.  You can scroll through the results OR you could pipe the output to `grep`, which will do that for you.

```sh
$ strings warm |grep pico
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_d6969390}
```
**picoCTF{b1scu1ts_4nd_gr4vy_d6969390}**
