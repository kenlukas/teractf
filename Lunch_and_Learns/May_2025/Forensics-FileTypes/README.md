# File types

## Forensics

### This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

This challenge came with a file.

I tried opening it in a browser and it was NOT a pdf file.

```sh
file Flag.pdf
Flag.pdf: shell archive text
```
Okay this challenge is starting out very old school.  This is a self-extracting archive.  I can honestly say, I've never used it.  Here are more details:
[shar (file format)](https://en.wikipedia.org/wiki/Shar_(file_format))
[What is a Shell Archive](https://lowfatlinux.com/linux-shell-archives.html)

```sh
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2023-03-16 01:40 UTC by <root@e023b7dee37c>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
```
If you follow the instructions this is the outcome:
NOTE: I had to install uudecode in my environment.

```sh
$ sh Flag.pdf 
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

I tried to `cat` the file and it wasn't the decoded flag but it wasn't the same as before either.
```sh
$ file flag
flag: current ar archive
```

Great!  Another encoding method that isn't normally used.
[ar(UNIX)](https://en.wikipedia.org/wiki/Ar_(Unix))

```sh
$ ar x flag
```
This didn't have any response (good or bad).  Running the `file` command again, there were changes:

```sh
$ file flag
flag: cpio archive; device 234, inode 37426, mode 100644, uid 0, gid 0, modified Thu Mar 16 01:40:17 2023, 510 bytes "flag"
```

Wow, they are really leaning into the oddball archiving commands.

[cpio](https://en.wikipedia.org/wiki/Cpio)

```sh
$ cpio -i < flag
cpio: flag not created: newer or same age version exists
2 blocks

(lsiopy) abc@ffce7aecc25b:~$ mv flag flag.cpio

(lsiopy) abc@ffce7aecc25b:~$ cpio -i < flag.cpio
2 blocks
```

Okay, it wouldn't overwrite itself like the others did.  So I just renamed it and ran it again.

```sh
$ file flag
flag: bzip2 compressed data, block size = 900k
```

Well at least this uses a compression tool used in this century...

```sh
$ bzip2 -d flag
bzip2: Can't guess original name for flag -- using flag.out
$ file flag.out
flag.out: gzip compressed data, was "flag", last modified: Thu Mar 16 01:40:17 2023, from Unix, original size modulo 2^32 327
```

I'm beginning to hate this challenge :rage:

```sh
$ gunzip flag.out
gzip: flag.out: unknown suffix -- ignored
$ mv flag.out flag.gz
$ gunzip flag.gz
$ file flag
flag: lzip compressed data, version: 1
```

Yeah, I'm really feeling the rage :rage: :rage:

[lzip manual](https://www.nongnu.org/lzip/manual/lzip_manual.html)

```sh
$ lzip -d flag

$ file flag
flag: cannot open `flag' (No such file or directory)

$ ls -l
[ REDACTED for Brevity ]
-rw-r--r-- 1 abc abc     282 May 30 15:21 flag.out
[ REDACTED for Brevity ]

$ file flag.out
flag.out: LZ4 compressed data (v1.4+)
```

:crying:

```sh
$ mv flag.out flag.lz4

$ lz4 -d flag.lz4 
Decoding file flag 
flag.lz4                       : decoded 265 bytes                             

$ file flag
flag: LZMA compressed data, non-streamed, size 254

```

```sh
$ 7z e flag

7-Zip 24.09 (arm64) : Copyright (c) 1999-2024 Igor Pavlov : 2024-11-29
 64-bit arm_v:8-A locale=en_US.UTF-8 Threads:10 OPEN_MAX:1048576, ASM

Scanning the drive for archives:
1 file, 265 bytes (1 KiB)

Extracting archive: flag
--
Path = flag
Type = lzma
Method = LZMA:23

Everything is Ok

Size:       254
Compressed: 265

$ file flag~
flag~: lzop compressed data - version 1.040, LZO1X-1, os: Unix
```

```sh
$ lzop -d flag.lzop -o flag
lzop: flag: already exists; not overwritten

$ rm flag

$ lzop -d flag.lzop -o flag

$ file flag
flag: lzip compressed data, version: 1
```

Oh come on!  FFS! At this point I felt like I got turned around and redid a file.

```sh
$ lzip -d flag

$ file flag
flag: cannot open `flag' (No such file or directory)

(lsiopy) abc@ffce7aecc25b:~$ file flag.out
flag.out: XZ compressed data, checksum CRC64

```

:rage: :rage: :rage: :rage:

```sh
$ 7z e flag.out

7-Zip 24.09 (arm64) : Copyright (c) 1999-2024 Igor Pavlov : 2024-11-29
 64-bit arm_v:8-A locale=en_US.UTF-8 Threads:10 OPEN_MAX:1048576, ASM

Scanning the drive for archives:
1 file, 156 bytes (1 KiB)

Extracting archive: flag.out
--
Path = flag.out
Type = xz
Physical Size = 156
Method = LZMA2:23 CRC64
Streams = 1
Blocks = 1

Everything is Ok

Size:       110
Compressed: 156

(lsiopy) abc@ffce7aecc25b:~$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37396230316332367d0a
```

Finally!!

```sh
$ cat flag | xxd -r -p
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```

**picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}**
