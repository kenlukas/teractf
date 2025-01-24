# Big Zip

## General

### Unzip this archive and find the flag.


```sh
$ wget https://artifacts.picoctf.net/c/505/big-zip-files.zip
--2025-01-24 10:55:20--  https://artifacts.picoctf.net/c/505/big-zip-files.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 2600:9000:27cb:3800:16:5ec5:2840:93a1, 2600:9000:27cb:9a00:16:5ec5:2840:93a1, 2600:9000:27cb:3a00:16:5ec5:2840:93a1, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|2600:9000:27cb:3800:16:5ec5:2840:93a1|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3182988 (3.0M) [application/octet-stream]
Saving to: ‘big-zip-files.zip’

big-zip-files.zip             100%[==============================================>]   3.04M  --.-KB/s    in 0.1s    

2025-01-24 10:55:20 (25.2 MB/s) - ‘big-zip-files.zip’ saved [3182988/3182988]

                                                                                                                     
$ ls -la
total 3120
drwxrwxr-x  2 kenny kenny    4096 Jan 24 10:55 .
drwxrwxr-x 10 kenny kenny    4096 Jan 24 10:55 ..
-rw-rw-r--  1 kenny kenny 3182988 Aug  4  2023 big-zip-files.zip
                                                                                                                     
$ unzip big-zip-files.zip 
Archive:  big-zip-files.zip
   creating: big-zip-files/
 extracting: big-zip-files/jpvaawkrpno.txt  

[ A Lot of Unzip Text Redacted ]

$ ls -la
total 3160
drwxrwxr-x   3 kenny kenny    4096 Jan 24 10:55 .
drwxrwxr-x  10 kenny kenny    4096 Jan 24 10:55 ..
drwxrwxr-x 121 kenny kenny   36864 May  3  2020 big-zip-files
-rw-rw-r--   1 kenny kenny 3182988 Aug  4  2023 big-zip-files.zip
                                                                                                                     
$ grep -R pico big-zip-files/*
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```                                                                                                                     
**picoCTF{gr3p_15_m4g1c_ef8790dc}**
