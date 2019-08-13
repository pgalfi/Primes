from math import sqrt

from bitarray import bitarray


def get_primes(n, start=1, count=None, page=1):
    if n < 2:
        return ()
    primes = bitarray(n)
    primes.setall(True)
    primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] is True:
            for j in range(i * i, n, i):
                primes[j] = False
    if count is None:
        return [i for i in range(start, n) if primes[i]]
    return [i for i in range(start, n) if primes[i]][(page-1) * count: page * count]
