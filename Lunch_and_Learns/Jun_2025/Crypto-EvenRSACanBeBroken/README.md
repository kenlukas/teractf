# Even RSA Can Be Broken???

## Cryptography

### This service provides you an encrypted flag. Can you decrypt it with just N & e?  Connect to the program with netcat: $ nc verbal-sleep.picoctf.net 58750 

When you connect to the endpoint you'll get something similar to the following.  Note: It changes each time you hit the endpoint.

```sh
$ nc verbal-sleep.picoctf.net 58750
N: 16373454727922507934274730837153493097115046145122730498680558425685970406276795385247018981195849489942368561038528954318167103751942839664327554287037098
e: 65537
cyphertext: 763559525850305696903462512495094075868893204294612496667090588433311227380058567940061224577931220368096084889108203592892736690047197987138054822047559

```
Normally, I'd feed these values into RSACtfTool, but since N is even, the tool is having a fit.  So we need to do this the old-fashioned way.
But let's back up a bit.  To oversimplify, RSA works by using two unique prime numbers of sufficient length, which are denoted as p and q.  Those primes are multiplied together to give a value N.  Another smaller prime number (usually 65537) is chosen as an exponent value.  The last step before encrypting is to convert the text you want to encrypt to an integer, which we'll call m. To encrypt, get the value of m to the e power (m^e) and find the modulo of N for that value.  That is your ciphertext (ct).  ct = m<sup>e</sup> mod N

I'm not qualified or competent enough to go into the mathematical details of how to decrypt.  To decrypt the ciphertext, you need a value commonly referred to as 'phi', which is also called Euler's totient, and another called 'd', which is the modulo inverse of 'e'.  Phi is equivalent to (p-1)*(q-1).  Then, you need to obtain the private exponent, which can be calculated using the mod_inverse function in the Python Sympy library. If you're interested, d is the modular inverse of e modulo phi(n).


```python
#!/usr/bin/env python3

from sympy import factorint, mod_inverse, isprime

# int() doesn't do anything if the value is already an integer 
n = int(17674588416444612204334207654890370235816263111751643177108130032186709372444998997950000215459405634510788767588983166839871976320732985836549601787763418)
e = int(65537)
ct = int(16800736516425931651701294699767515179504993743102916190484835681412438330649339822983508667151572571229055433843649030514303915745361524950163817126361567)

# Since n is even this will have 2 as a factor)
p, q = factorint(n)

if isprime(p) and isprime(q):
    # I'd like to just assign phi as p or q minus 1 but since I don't know which is 2 it's easier to just multiply them
    phi = (p-1)*(q-1)
    d = mod_inverse(e, phi)
    dt = pow(ct, d, n)

    dec_str = dt.to_bytes((dt.bit_length() + 7) // 8, byteorder = "big")
    print(f'{dec_str.decode()}')
else:
  print(f'p and q are not primes')


