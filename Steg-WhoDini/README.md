# Whodini

## Steg

### "Oh my god, it's him, not again!" This guy took the flag!  "I have zero doubts!" He's  Shady, and probably hid the flag under lock and key.

This image didn't have anything interesting in the output of `strings` or exiftool.  I ran steghide on it and it looks to be password protected.

Run `stegseek --crack`.  It provides the password and outputs the flag file.

```sh
$ stegseek --crack -sf Eminem-2017-album.jpg 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "Abracadabra"      
[i] Original filename: "flag.txt".
[i] Extracting to "Eminem-2017-album.jpg.out".

```

**teractf{w1LL_th3_r34L_5L1m_5h4dy_pL34s3_5t4nd_up}**
