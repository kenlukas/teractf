import Crypto.Util.number as cr
import math

message = b"flag{super_duper_fake_flag}"

m = int.from_bytes(message, "big")

# Saving time generating primes!
p = cr.getPrime(1024)
e = 65537

n = p * p

enc_mess = pow(m, e, n)

print(f"e = {e}")
print(f"n = {n}")
print(f"enc_mess = {enc_mess}")

