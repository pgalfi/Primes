from math import sqrt, trunc

from bitarray import bitarray

primes = bitarray([False, False])  # numbers 0 and 1 are not prime


def get_primes(n, start=1, count=None, page=1):
    if n < 2:
        return ()
    prev_n = primes.length() - 1
    if n > prev_n:
        part = bitarray(n - prev_n)
        part.setall(True)
        primes.extend(part)

    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] is True:
            for j in range(max(i * i, i * (trunc(prev_n / i) + 1)), n+1, i):
                primes[j] = False
    if count is None:
        return [i for i in range(start, n) if primes[i]]
    return [i for i in range(start, n) if primes[i]][(page - 1) * count: page * count]


def get_primes_old(n, start=1, count=None, page=1):
    if n < 2:
        return ()
    local_primes = bitarray(n)
    local_primes.setall(True)
    local_primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if local_primes[i] is True:
            for j in range(i * i, n, i):
                local_primes[j] = False
    if count is None:
        return [i for i in range(start, n) if local_primes[i]]
    return [i for i in range(start, n) if local_primes[i]][(page-1) * count: page * count]