from constants import PASSWORD_HASH, PASSWORD_LENGTH, TOTAL_CHARS
from multiprocessing import cpu_count
from hashlib import sha384
from itertools import permutations
from time import time

print(f"\nCores available: {cpu_count()}\n")

t = time()
possible_passwords = permutations(
    TOTAL_CHARS, PASSWORD_LENGTH)
print("Processing...")

for password in possible_passwords:
    password_hash = sha384(''.join(password).encode('utf-8')).hexdigest()

    if (PASSWORD_HASH == password_hash):
        print(f"Password is: {''.join(password)}")
        break

seconds = round(time() - t)
print(f"Time spent: {seconds} seconds")
