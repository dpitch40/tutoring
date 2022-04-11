import random
import time
import argparse

def is_even(n):
    # Simulate network call
    time.sleep(random.uniform(0.5, 5))

    return n % 2 == 0

def check_is_even(integers):
    print(integers) # TODO

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('integers', type=int, nargs='+', help='')
    args = parser.parse_args()

    check_is_even(args.integers)

if __name__ == '__main__':
    main()
