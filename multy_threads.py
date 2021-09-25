from helpers import async_find_password
from constants import CPUS_AVAILABLE, TOTAL_CHARS, TOTAL_CHARS_LEN
from multiprocessing import Event, Process
import sys
import re


if __name__ == "__main__":
    attempts = []
    event = Event()

    chunks_count = int(TOTAL_CHARS_LEN / CPUS_AVAILABLE)
    chunks = re.findall('.' * chunks_count, TOTAL_CHARS)

    print('Processing...')

    for i in range(CPUS_AVAILABLE):
        p = Process(target=async_find_password,
                    args=(event, chunks[i]))
        p.start()
        attempts.append(p)

    while True:
        if event.is_set():
            for i in attempts:
                i.terminate()
                sys.exit(1)
