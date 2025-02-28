# First Find

## General

### Unzip this archive and find the file named 'uber-secret.txt'

Right-click on the link and use `wget` to download it into your environment.

Unzip it using the unzip command:  `unzip files.zip`

This will create a bunch of directories and files under the `files` directory.

The `find` command is extremely useful in finding files by name, type, size, permissions, or a combination of those.  Because of the title of the challenge, we'll use the `find` command to locate the file referenced in the challenge.  You could just use `grep -r pico *` to find the flag.

The `find` command uses the following syntax:  find <directory to start search> -name <file name>

This will search the directory tree starting with the directory in the command and will return any matches.  There are a couple of different ways to handle the matches.  You could use the -exec switch in find and use the `grep` command and search for the picoCTF string, or you could `cat` the file. Or you could pipe the output to the `xargs` command and run command against the name.

Examples:

`find files/ -name uber-secret.txt -exec cat {} + `  
`find files/ -name uber-secret.txt -exec grep pico {} +`  
`find files/ -name uber-secret.txt |xargs -I {} cat {}`  
`grep -r picoCTF files/*`

```sh
$ find files/ -name uber-secret.txt              
files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt

$ find files/ -name uber-secret.txt -exec grep pico {} +
picoCTF{f1nd_15_f457_ab443fd1}

$ find files/ -name uber-secret.txt -exec cat {} +
picoCTF{f1nd_15_f457_ab443fd1}

$ find files/ -name uber-secret.txt |xargs -I {} cat {}
picoCTF{f1nd_15_f457_ab443fd1}

$ grep -r picoCTF files/*
files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
```

**picoCTF{f1nd_15_f457_ab443fd1}**
