#!/usr/bin/env python3
""" Factor numbers """
from sys import argv


def open_read_file(file_name):
    """read from file
    add to array
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    number_to_factor = []
    for line in lines:
        number_to_factor.append(int(line))
    return number_to_factor


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d


def factorize(n):
    if n < 2:
        return []

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        else:
            factor = pollards_rho(n)
            factors.append(factor)
            n //= factor

    return factors


def factorint(n):
    factors = factorize(n)
    factor_dict = {}
    for factor in factors:
        if factor in factor_dict:
            factor_dict[factor] += 1
        else:
            factor_dict[factor] = 1
    return factor_dict


def fac_list(ls):
    """factor each
    num in ls
    """
    for i in ls:
        factors = factorint(i)
        factor_str = " * ".join([f"{factor}^{exponent}" for factor, exponent in factors.items()])
        print(f"{i} = {factor_str}")


if len(argv) == 2:
    fac_list(open_read_file(argv[1]))
