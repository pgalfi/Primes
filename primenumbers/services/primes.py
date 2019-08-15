import time
from math import sqrt, trunc
from threading import Lock

from bitarray import bitarray

primes_sieve = {
    "array": bitarray([False, False]),  # numbers 0 and 1 are not prime
    "prev_n": 1,
    "access": Lock(),
}


def build_sieve(n):
    primes = primes_sieve["array"]
    print("allocating: ", primes_sieve["prev_n"], "-", n)
    part = bitarray(n - primes_sieve["prev_n"])
    part.setall(True)
    primes.extend(part)
    prev_n = primes_sieve["prev_n"]
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] is True:
            for j in range(max(i * i, i * (trunc(prev_n / i) + 1)), n + 1, i):
                primes[j] = False
    primes_sieve["prev_n"] = n


def apply_sieve(n, start):
    if n < 2:
        return []
    primes = primes_sieve["array"]
    return [i for i in range(start, n) if primes[i]]


def _primes_list_optional_lock(n, start=1):
    while n > primes_sieve["prev_n"]:
        if primes_sieve["access"].locked():
            time.sleep(0.1)
        else:
            primes_sieve["access"].acquire()
            build_sieve(n)
            primes_sieve["access"].release()

    return apply_sieve(n, start)


def _primes_list_always_lock(n, start=1):
    primes_sieve["access"].acquire()
    if n > primes_sieve["prev_n"]:
        build_sieve(n)
    primes_sieve["access"].release()
    return apply_sieve(n, start)


def paginate(page, page_size, primes_list, start):
    if page_size is None:
        return {"numbers": primes_list, "count": len(primes_list), "start": start, "page": page, "page_size": page_size}
    return {"numbers": primes_list[(page - 1) * page_size: page * page_size], "count": len(primes_list),
            "start": start, "page": page, "page_size": page_size}


def get_primes(n, start=1, page=1, page_size=None, locking="always"):
    if locking == "optional":
        primes_list = _primes_list_optional_lock(n, start)
    else:
        primes_list = _primes_list_always_lock(n, start)

    return paginate(page, page_size, primes_list, start)


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
