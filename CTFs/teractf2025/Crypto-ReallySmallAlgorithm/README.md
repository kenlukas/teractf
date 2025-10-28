# Really Small Algorithm

## Cryptography

### I've heard RSA should not use small values for p and q, but is it really that big of a deal?  Can you decrypt this?

> e = 65537
> n = 94578119332400975818394241460776087317764046016638164869801894001973540791573
> c = 3218281023452845471335080878750402623764031876923361337868267430803274119668

Looks easy enough, and this one is.  But, there's a caveat which I'll discuss in a minute.  I used the `rsactftool` to solve this.  The hardest part is getting the image to install correctly with all the Sage math pieces.  Running it spits out the answer...easy peasy.

But no, I reran the program I made to generate `p`, and `q` which gave a different value for `n`.  Notice in the solution below it says the `factordb` method was successful.  That solution uses the data in [factordb.com](https://factordb.com), if the value for `n` is in the database, then this method works.  Factordb is just what it says, a database for factors.  When my program reran, it failed because that value for `n` wasn't in the database.  Anyway, this is my solution:

```sh
$ docker run --rm rsactftool_full -e 65537 -n 94578119332400975818394241460776087317764046016638164869801894001973540791573 --decrypt 3218281023452845471335080878750402623764031876923361337868267430803274119668
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpo74h9pue.
[*] Performing system_primes_gcd attack on /tmp/tmpo74h9pue.
['/tmp/tmpo74h9pue']
attack initialized...
attack initialized...
100%|██████████| 7007/7007 [00:00<00:00, 692331.88it/s]
[+] Time elapsed: 0.0792 sec.
[*] Performing mersenne_primes attack on /tmp/tmpo74h9pue.
 24%|██▎       | 12/51 [00:00<00:00, 142987.64it/s]
[+] Time elapsed: 0.0015 sec.
[*] Performing pastctfprimes attack on /tmp/tmpo74h9pue.
[+] Time elapsed: 0.0009 sec.
[*] Performing rapid7primes attack on /tmp/tmpo74h9pue.
[+] Time elapsed: 0.0009 sec.
[*] Performing smallq attack on /tmp/tmpo74h9pue.
[+] Time elapsed: 0.3608 sec.
[*] Performing factordb attack on /tmp/tmpo74h9pue.
[*] Attack success with factordb method !             <------------------ This is what I was referring to
[+] Total time elapsed min,max,avg: 0.0009/0.3608/0.0887 sec.

Results for /tmp/tmpo74h9pue:

Decrypted data :
HEX : 0x746572616374667b6d616e6461743072795f7235615f7461356b5f667477217d
INT (big endian) : 52647531413873679896272851882470967919883758103837120738043696920754312913277
INT (little endian) : 56598236471996173456982608490647395716719848462099148058437070190777501640052
utf-8 : teractf{mandat0ry_r5a_ta5k_ftw!}
utf-16 : 整慲瑣筦慭摮瑡爰役㕲彡慴欵晟睴紡
STR : b'teractf{mandat0ry_r5a_ta5k_ftw!}'
```

**teractf{mandat0ry_r5a_ta5k_ftw!}**
