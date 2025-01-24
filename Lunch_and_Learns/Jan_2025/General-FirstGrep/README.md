# First Grep

## General

### Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

Step One: Right-click the link in the challenge and copy the address (or save link as)

Step Two: In your shell use the `wget` command: `wget https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file`

Since all challenges in picoCTF begin with `pico` use the `grep` command to search for it.

Step Three:  grep pico file

```sh
$ grep pico file
picoCTF{grep_is_good_to_find_things_dba08a45}
```

**picoCTF{grep_is_good_to_find_things_dba08a45}**


