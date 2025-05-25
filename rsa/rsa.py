from utils import gcd, mod_inverse, is_coprime

def generate_keys(p, q, e=65537):
    n = p * q
    phi = (p - 1) * (q - 1)

    if not is_coprime(e, phi):
        raise ValueError("e and phi(n) must be coprime!")

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(message, pub_key):
    e, n = pub_key
    return pow(message, e, n)

def decrypt(ciphertext, priv_key):
    d, n = priv_key
    return pow(ciphertext, d, n)
