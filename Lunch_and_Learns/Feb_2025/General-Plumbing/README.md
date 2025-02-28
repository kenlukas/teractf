# Plumbing

## General

### Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? 

As with almost all solutions using Linux there are multiple ways to solve this.

Use `netcat` to connect to the domain/port.  Text will scroll off the screen, telling you repeatedly that it's not a flag.

One way to solve this is just to scroll through the output to find it.

To see how many lines there are in the output use a "pipe" (see the reference to the challenge name), and a Unix command called wc which is short for word count.  The pipe command takes output from one command and uses it for another command.  To create a pipe use the `|` symbol.

```sh
nc jupiter.challenges.picoctf.org 7480 | wc -l 

10001
```
The `-l` with wc tells it to count lines...Ten thousand one in this challenge.

Since you know the flag will start with `pico` we can search for that, and we can use a command we've used before: grep!  Since we're piping content into grep we don't need to specify a filename, only the pattern we're looking for:

```sh
$ nc jupiter.challenges.picoctf.org 7480 |grep pico
picoCTF{digital_plumb3r_06e9d954}
```

Here are a few other ways to solve this challenge.  There is a redirect character `>` that will redirect the output to a file (NOTE: everything in Unix is a file)

```sh
$ nc jupiter.challenges.picoctf.org 7480 > plumbing.txt
```
What this does is send the output to a file named plumbing.txt  We can then use the `grep` command to search for the flag.

Another option would be to use the pipe and send the file to a command like `more` or `less`.   (NOTE: use `less` it's better on memory)

To use `less` use the pipe command to redirect the output into it.  It will only load a screenful of text.  Then type `/pico` and hit return.  The flag should be the top line on your screen.

**picoCTF{digital_plumb3r_06e9d954}**
