from rsa import generate_keys, encrypt, decrypt

# Small demo primes
p = 61
q = 53
message = 42

public_key, private_key = generate_keys(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

cipher = encrypt(message, public_key)
print("Encrypted:", cipher)

original = decrypt(cipher, private_key)
print("Decrypted:", original)
