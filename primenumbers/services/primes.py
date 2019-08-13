from math import sqrt, trunc
from threading import Lock

from bitarray import bitarray

primes = bitarray([False, False])  # numbers 0 and 1 are not prime
bitarray_access = Lock()


def _primes_list(n, start=1):
    if n < 2:
        return []
    prev_n = primes.length() - 1
    bitarray_access.acquire()
    if n > prev_n:
        part = bitarray(n - prev_n)
        part.setall(True)
        primes.extend(part)
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] is True:
            for j in range(max(i * i, i * (trunc(prev_n / i) + 1)), n + 1, i):
                primes[j] = False
    bitarray_access.release()
    return [i for i in range(start, n) if primes[i]]


def get_primes(n, start=1, page=1, page_size=None):
    primes_list = _primes_list(n, start)
    if page_size is None:
        return {"numbers": primes_list, "count": len(primes_list), "start": start, "page": page, "page_size": page_size}
    return {"numbers": primes_list[(page - 1) * page_size: page * page_size], "count": len(primes_list),
            "start": start, "page": page, "page_size": page_size}


# Below versions are obsolete, were kept only for testing and performance comparisons

def get_primes_version_01(n, start=1, page=1, size=None):
    if n < 2:
        return []
    local_primes = bitarray(n)
    local_primes.setall(True)
    local_primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if local_primes[i] is True:
            for j in range(i * i, n, i):
                local_primes[j] = False
    if size is None:
        return [i for i in range(start, n) if local_primes[i]]
    return [i for i in range(start, n) if local_primes[i]][(page - 1) * size: page * size]


def get_primes_naive(n, start=1, page=1, size=None):
    if n < 2:
        return []
    local_primes = [2]
    if start % 2 == 0:
        start += 1
    for i in range(max(3, start), n, 2):
        is_prime = True
        for j in range(3, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            local_primes.append(i)
    if size is None:
        return local_primes
    return local_primes[(page - 1) * size: page * size]
