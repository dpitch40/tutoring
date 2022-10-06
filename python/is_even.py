import random
import time
from concurrent.futures import *

def is_even(n):
    # Simulate network call
    time.sleep(random.uniform(0.5, 5))

    return n % 2 == 0

def check_is_even(integers):
    with ThreadPoolExecutor(max_workers=100) as executor:
        future = executor.map(is_even, integers)
        print(list(future))

def main(stuff):
    check_is_even(stuff)

