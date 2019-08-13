#### Prime generation algorithms

1. Naive approach: loop through all k numbers for n > k > 2 and check if n is divisible by k.
* CPU: Very slow on large numbers, complexity is exponential
* Memory: almost no memory footprint, no storage
* No concurrency issues as there is no storage

2. Memorize: keep a memory of all previous primes and only check if new number if divisible with a previous prime
* CPU: better as the number of compares on all previous primes is less
* Memory: ever expanding storage of previous prime numbers, but it is also a cache, so a call to n, means that all possible primes smaller than n get computer and stored, so any subsequent calls with smaller number would get retrieved from the cache.
* Concurrency: Race conditions may occur on the data structure where concurrent threads may try to add primes to the memory

3. Use a bit array as a sieve and apply known mathematical optimizations to the range of prime numbers to be checked to determine if new number if prime.
* CPU: less number of operations due to the mathematical optimizations
* Memory: n x 1 bit storage for the sieve.
* Concurrency: the bit array could be shared and maintained

4. Use a segmented sieve to reduce storage requirements -- not implemented for this exercise. 
 
 