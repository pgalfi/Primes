## Prime Numbers JSON API

The scope of this implementation is to provide as per the requirement a simple REST JSON API endpoint that will return a list of prime numbers based on the provided query parameters.


### Prime number generation service

A service implementation is needed that will generate all primary numbers from 1 to  *n* (provided as query parameter). The number 1 is excluded from the list as per definition: https://en.wikipedia.org/wiki/Prime_number

Multiple options were examined for the implementation:

**Naive approach:** loop through all k numbers for 2 < k < n and check if k is divisible by any previous number.
* CPU: Extremely slow on large numbers, complexity is exponential
* Memory: almost no memory footprint, no storage
* No concurrency issues as there is no storage

**Memorize earlier primes:** store all previous primes and only check if a new number if divisible with any previous prime number.
* CPU: better as the number of compares on all previous primes is less
* Memory: all previous prime numbers need to be stored, but it is also a cache, so a call to n, means that all possible primes smaller than n get computed and stored, so any subsequent calls with smaller number would get retrieved from the cache.
* Concurrency: Race conditions may occur on the data structure where concurrent threads may try to add prime numbers to the memory

**Bit array sieve:** use a bit array as a sieve and apply known mathematical optimizations to the range of prime numbers to be checked to determine if a new number if prime.

* CPU: less number of operations due to the mathematical optimizations
* Memory: n x 1 bit storage for the sieve, expands for higher n numbers.
* Concurrency: the bit array can be shared and maintained while being built up by requests

**Possible further optimization**: Implement concurrency resource locks to only block the part of the bit array that is being modified (part getting expanded) while allowing the already computer part accessed and read by concurrent requests.
 
### JSON API endpoint

Django framework was used to build a simple endpoint to serve the prime numbers. Following the standards laid out by the framework a simple view was set up (views.py) and wired into URL endpoint using the frameworks' tools (urls.py).

Query parameter validation was set up through a simple form logic that wires in the framework's validation and error handling logic for the specified parameter fields. The form was implemented in forms.py.

The API accepts the following query parameters:

**n** - the upper integer limit for prime number generation

**start** - the starting point for integer generation (optional, defaults to 1)

**page_size** - the amount of numbers a single API call will return (defaults to 100)

**page** - specify which page of numbers to be returned from the total list of generated prime numbers (optional, defaults to 1)

### Deployment

The project requires Python 3.7 installation on the system. It can be downloaded as a complete zip package from this location:

https://drive.google.com/open?id=1kX1AK2_cADzo6mpcyhRYQjUrLoFmpByr

Once unpacked, the following commands can be executed from the folder of the project:

```
venv\scripts\activate

python manage.py test primenumbers
python manage.py runserver
```

The above will activate a virtual environment that contains all required dependencies, run all unit tests and then start the dev server that can be accessed on port 8000 to test the API.

The project can also be pulled as a docker image from here:

```
docker pull pgalfi/assignments:primes
```

