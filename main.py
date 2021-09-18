from multiprocessing import cpu_count
from hashlib import sha384
from itertools import permutations
from time import time

PASSWORD_HASH = "2b697b9f191f2299c2b7fb5caeb1cae4bb2fe2bab7387d01bf8e91840d3064a827b99c5470b20bc4cb2199f0180cd4e2"
PASSWORD_LENGTH = 6
UPPER_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = "!@#$%^&*_-"

print(f"\nCores available: {cpu_count()}\n")

t = time()
possible_passwords = permutations(
    UPPER_CHARS + SPECIAL_CHARS, PASSWORD_LENGTH)
print("Processing...")

for password in possible_passwords:
    password_hash = sha384(''.join(password).encode('utf-8')).hexdigest()

    if (PASSWORD_HASH == password_hash):
        print(f"Password is: {''.join(password)}")
        break

seconds = round(time() - t)
print(f"Time spent: {seconds} seconds")
