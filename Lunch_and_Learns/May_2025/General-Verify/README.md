# Verify

## General

### People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

> Checksum: 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
> To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.

The simplest way to do this challenge (in my opinion) is to try to decrypt every file and look for the flag in the results.

```sh
for f in ./files/*; do 
  ./decrypt.sh $f |grep pico;
done
```
The output is a mess but it's easy to see the flag in all the noise.

This is a little more elegant:

```sh
for file in files/*; do 
  checkit=$(sha256sum "$file"); 
  if [[ "$checkit" =~ ^55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a ]]; then 
    output=$(./decrypt.sh "$file");
    echo $output;
    break;
  fi; 
done
```

**picoCTF{trust_but_verify_2cdcb2de}**
