import sys
from functools import reduce
from math import sqrt
import itertools

def factors_1(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

def isprime(n, lp):
    for i in lp:
        j = int(i)
        if n % j == 0:
            if j == n:
                return 1
            return j
    divs = range(1000001, int(n ** 0.5) + 1, 2)
    return [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0][0]

def sieve_erathosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x, y, d = 2, 2, 1
    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def primef(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    lp = sieve_erathosthenes(1000000)  # You need to generate a list of primes
    lpi = []
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        for line in lines:
            lpi.append(int(line))
    for i in lpi:
        j = primef(i)  # Assuming factor(i, lp) returns the prime factor
        print("{}={:d}*{}".format(i, i//j, j))
