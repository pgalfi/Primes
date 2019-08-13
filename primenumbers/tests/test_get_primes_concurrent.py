import threading
from unittest import TestCase

from primenumbers.services.prime_generator import get_primes


def test_concurrently(times):
    def test_concurrently_decorator(test_func):
        def wrapper(*args, **kwargs):
            exceptions = []

            def call_test_func():
                try:
                    test_func(*args, **kwargs)
                except Exception as e:
                    exceptions.append(e)
                    raise

            threads = []
            for i in range(times):
                threads.append(threading.Thread(target=call_test_func))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            if exceptions:
                raise Exception('test_concurrently intercepted %s exceptions: %s' % (len(exceptions), exceptions))

        return wrapper

    return test_concurrently_decorator


class TestGetPrimesConcurrent(TestCase):

    @test_concurrently(5)
    def test_concurrent_01(self):
        self.assertEqual(78498, len(get_primes(1000000)))  # 1s 202ms -- one time execution time is 600ms

    @test_concurrently(10)
    def test_concurrent_02(self):
        self.assertEqual(78498, len(get_primes(1000000)))  # 1s 475ms -- one time execution is 600ms


