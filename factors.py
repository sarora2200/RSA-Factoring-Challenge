#!/usr/bin/python3

import math
import sys
import time

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i

def main(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
