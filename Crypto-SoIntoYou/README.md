# So Into You

## Crypto

### Atlanta Rhythm Section?  ARS?  I think the acronym might be scrambled.  It's "prime" time for you to figure out the flag.

This is poorly implemented RSA.  You should never use the same prime number for p and q.  The normal method for encrypting something with RSA is to get two large primes (4096?) and multiply them together to get `n`.  The way this version is implemented, `p` can be found by getting the square root of `n`.  A good implementation of RSA will not give you `p` and `q` by taking the square root of `n`.

If you have `p` (and `q`), you can calculate `phi`.  With `phi` you can decrypt the encrypted message. 

The `e` is a public key.  It's normally set to 65537.  Smaller numbers could be used but that weakens the encryption.

If `m` is the integer value of a byte string, the encrypted message is calculated by  m<sup>e</sup> mod n.

In Python, it's `pow(m , e, n)`

The values for `n` and `e` are included in the output.txt file.  It also includes the encrypted message.  To reverse it, you need to calculate `phi` and then compute the modular multiplicative inverse.  That is `e`<sup>-1</sup> mod `phi`.  In python, `pow(e, -1, phi)`

Phi is (p - 1) * (q - 1).  Phi must be different values.  So for the bad_rsa, you can't do (p - 1) * (p - 1).  Instead use p * (p - 1).

```python
import Crypto.Util.number as cr_num
import math

e = 65537
n = 26503520532087622782456250389978802036067679966552706124563108417354971624009464915606596396806568119643766876810699947981056277117338661887579022423916822982380765669178195178181310064457522179960988110363698431698109301157257225202895090575489967739352211986928868266478879827994194610120156803614001611522207944734284550451336622841069599287893059521383458703965685164817037384101821690605125739472246919336671285133805384844960451006031707127762886867180298316028253978559037958007191722071798748978589954081759145606475738629273768661175863857086492099332698212358799309443714831959748145764859518032138469940369
enc_mess = 7295370736488422707526183473643217263808395516396131011297575291349065623618549710161952609040055701924052724542498797041463993009999897399449180167705873486605569373288796553058460450571312091477774214221145432911047038913096650173822812910831839127702667819360519071961735328629958348998159529191168856842355963580944147276474916566140117687789236619820164315544656109018766222892860424702319100297555650473960705438473154606842123427878427263183839573821001615717779563108958547612312322716919747373280347048058004741345449839875403578554721471847314249707943034637562345311916222044445655761857875954218411857291

# Since n is p squared, calculate the square root of n
p = math.isqrt(n)

# phi cannot be the same value so alter one.
phi = p * (p - 1)
d = pow(e, -1, phi)

#Decrypt the message
d_mess = pow(enc_mess, d, n)
# convert it back to bytes from int
flag = d_mess.to_bytes((d_mess.bit_length() + 7) // 8, "big")
print(flag)
```
**teractf{th3r3_wa5_v00d00_1n_th3_v1b3}**
