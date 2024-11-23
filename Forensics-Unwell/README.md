# Unwell

## Forensics

### I was investigating a flag that disappeared as if by magic, but all I found was this file and a note:  "I know right now you can't tell, but stay awhile and maybe then you'll see a different side of me."

If you try to open the file you'll (hopefully) get an error.

![file error](./file_error.png)

The clue alludes to magic, as in the [files magic number.](https://en.wikipedia.org/wiki/Magic_number_(programming))

A .png file should start with `89 50 4E 47` but this file starts with `88 49 4D 46` (off by one).  If you change the first four bytes to the expected value the flag appears...like magic. :tophat: :sparkles:

![unwell](./unwell.orig.png)

**teractf{1m_ju5t_4_L1ttL3_unw3LL}**
