def gen_primes(n):
    D = {}
    q = 2
    while q < n:
        if q not in D:
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        if n % int(q) == 0:
            yield q
            break
        q += 1

for i in gen_primes(2497885147362973):
    print(i)
    break
