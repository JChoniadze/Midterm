from cryptography.hazmat.primitives.asymmetric import dh

# Step 1: Generate DH parameters
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Step 2: Alice generates private/public key
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

# Step 3: Bob generates private/public key
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Step 4: Exchange public keys and compute shared secret
alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_shared_key = bob_private_key.exchange(alice_public_key)

# Step 5: Print and compare shared keys
print("Alice's shared key:", alice_shared_key.hex())
print("Bob's shared key:  ", bob_shared_key.hex())

# Step 6: Validate if they match
assert alice_shared_key == bob_shared_key
print("✅ Shared keys match!")
