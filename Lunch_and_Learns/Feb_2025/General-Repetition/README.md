# Repetition

## General

### Can you make sense of this file?

Download the file and see what type of file it is.

```sh
$ file enc_flag 
enc_flag: ASCII text
```
Seeing it's an ASCII file, `cat` it

```sh
$ cat enc_flag 
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKVVZXcE9VazFXV2toT1dHUllDbUY2UWpSWk1GWlhWa2RHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

In general, when I see equal signs at the end of a string, I think Base64.  Normally, I'd open this file in CyberChef and use the From Base64 recipe.  But to solve this only using Linux, my strategy would be to `cat` the file and pipe the output to `base64` and use the decode options (-d).

```sh
$ cat enc_flag |base64 -d
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JUVWpOUk1WWkhOWGRYCmF6QjRZMFZXVkdGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
```
More equal signs at the end of text means it's probably more base64.  Pipe the output from the previous command to base64 again.

```sh
$ cat enc_flag |base64 -d |base64 -d
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BTUjNRMVZHNXdX
azB4Y0VWVGFteEVXbm93T1VOblBUMEsK
```
Okay, I see where this is going, the challenge name foreshadowed this.  SIDE NOTE: In a CTF, most challenge names are a hint.

I'm not going to show every iteration of this, from the following you can see this was encoded six times with base64.

```sh
$ cat enc_flag |base64 -d |base64 -d |base64 -d |base64 -d |base64 -d |base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}
```

**picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}**
