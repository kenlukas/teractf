# Nice netcat...

## General

### There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 35652, but it doesn't speak English...

When you connect to this site it prints out a bunch of numbers.

To be successful at CTFs, you need to recognize numeric representations (decimal, hexidecimal, and octal) of alphanumeric characters.

I rely on [https://asciitable.com](https://asciitable.com) to help me manually translate to and from printable characters.

The first number in the output is 112.  If you look at the ASCII table you'll see it is the decimal representation of the lowercase p.  The number 105 is an i, and 99 is a c.  This is the flag in numeric value.

Now, how do you translate this?  You could copy and paste the output into CyberChef (and for speed I'd probably do that) but that's not automated.  Let's use the pipe and a super powerful command in Unix named `awk`. Awk stands for...nothing.  It's the initial of the lastname of the inventors.  It's great for data extraction and transformation.  Full disclosure, I don't use awk much anymore so I had to google this answer.

The %c will print a character based on it's ASCII value.

```sh
$ nc mercury.picoctf.net 35652 |awk '{printf("%c", $1)}'
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
```

**picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}**
