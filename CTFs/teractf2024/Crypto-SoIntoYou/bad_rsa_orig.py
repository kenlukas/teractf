import Crypto.Util.number as cr
import math

message = b"teractf{th3r3_wa5_v00d00_1n_th3_v1b3}"

m = int.from_bytes(message, "big")

# Saving time generating primes!
p = cr.getPrime(1024)
e = 65537

n = p * p
phi = p * (p - 1)

d = pow(e, -1, phi)

assert(e * d) % phi == 1
assert math.gcd(e, phi) == 1

enc_mess = pow(m, e, n)

print(f"e = {e}")
print(f"n = {n}")
print(f"enc_mess = {enc_mess}")

decrypted_m = pow(enc_mess, d, n)
decrypted_mess = decrypted_m.to_bytes((decrypted_m.bit_length() + 7) // 8, "big")

print(decrypted_mess)
