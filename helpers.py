from itertools import permutations
from multiprocessing import Event
from constants import PASSWORD_HASH, PASSWORD_LENGTH, TOTAL_CHARS, TOTAL_CHARS_LEN
from hashlib import sha384
import time


def hashes_match(hash: str, possible_password):
    password_hash = sha384(
        ''.join(possible_password).encode('utf-8')).hexdigest()

    if password_hash == hash:
        return True

    return False


def async_find_password(event: Event, chunk: str):
    t = time.time()
    password_parts = permutations(TOTAL_CHARS, PASSWORD_LENGTH - 1)

    for part in password_parts:
        for char in chunk:

            password = ''.join(part) + char

            if hashes_match(PASSWORD_HASH, password):
                t = time.time() - t
                print(
                    f"Password is: {password}\nTime spent: {round(t, 5)} seconds")
                event.set()
                return True
