# 2 Legit 2 Quit

##  Forensics

### I created a flag in another users repo by mistake.  I deleted the fork but they told me it's still there!  Can you "Hammer" on this for a bit?  Oh, the repo is https://github.com/lukasew/nothing2see.  This is too le-Git too quit. Oh, I think my commit id started with 'e'.

This "vulnerability" is by design in Git.  The TL;DR for this challenge is that a commit on a repo clone will live on even if you delete it.  To try this at home, clone a repo, make a commit to your local copy, and delete it the clone.  If you search for the commit hash in the original repo you'll find your commit!  

The issue is if I put things like passwords, or Cloud account credentials in the clone and committed them, they are search able in the original repo.  Randomly searching would be difficult and Git will eventually rate limit or ban you from searching.  If you have the beginning of the commit hash, for instance the letter `e` you only need to find a few more characters.

There is a John Hammond [video about this](https://youtu.be/DYdMXwDfRdA)

I wrote this script to search for the beginning of the commit id:

```python
import itertools
import requests

# Hex characters"
chars = 'abcdef0123456789'

# This returns all possible `length` character string combinations of `chars` 
#   e.g. for "ab", 2 would produce aa, ab, ba, bb
def all_possible(chars, length):
    yield from itertools.product( *([chars] * length))

# Iterate a combination of 3 hex characters prepend the letter `e` to the beginning, look for non-404 status
for p in all_possible(chars, 3):
    short_hash = 'e' + ''.join(p)
    url = f"https://github.com/lukasew/nothing2see/commit/{short_hash}"
    r = requests.get(url)

    print(f"trying {short_hash}...")

    if r.status_code != 404:
        print(f'Short hash {short_hash} gave status {r.status_code} for URL {r.url}')
        break
```

Running it eventually finds the commit:

```sh
trying edab...
trying edac...
trying edad...
trying edae...
Short hash edae gave status 200 for URL https://github.com/lukasew/nothing2see/commit/edae
```
Commit id edaeb6e36f31b7f5b5b8f5de3ec8fa52771ff819

![pull_request](./pull_request.png)

**teractf{h4mm3r_d0nt_hurt_th3m}**

