# Strings It

## General

### Can you find the flag in file without running it?

This is pretty straightforward, and the challenge name is a huge clue.
Download the file using wget or curl and run `strings` against it.

```sh
$ strings -n 8 strings |grep pico
picoCTF{5tRIng5_1T_7f766a23}
```

**picoCTF{5tRIng5_1T_7f766a23}**
