import threading
import time
from unittest import TestCase

from primenumbers.services.primes import get_primes


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


def concurrent_with_params(*params):
    start = time.time()
    def wrapped_with_arguments(test_method):

        def wrapper(*args, **kwargs):
            exceptions = []
            threads = []

            def call_with_thread(*arguments):
                print("called service with", arguments[1:])
                try:
                    test_method(*arguments)
                except Exception as e:
                    exceptions.append(e)
                    raise
                end = time.time()
                print(arguments[1:], ">>>", end-start)
            if params is None:
                threads.append(threading.Thread(target=call_with_thread))
            else:
                for parameter in params:
                    threads.append(threading.Thread(target=call_with_thread, args=(args[0], parameter)))

            for t in threads: t.start()
            for t in threads: t.join()
            if exceptions:
                raise Exception('test_concurrently intercepted %s exceptions: %s' % (len(exceptions), exceptions))

        return wrapper

    return wrapped_with_arguments


class TestGetPrimesConcurrent(TestCase):

    @test_concurrently(5)
    def test_concurrent_01(self):
        self.assertEqual(78498, get_primes(1000000, locking="always")["count"])
        # 1s 200ms -- one time execution time is 600ms

    @test_concurrently(10)
    def test_concurrent_02(self):
        self.assertEqual(78498, get_primes(1000000, locking="always")["count"])
        # 1s 800ms -- one time execution is 600ms

    def test_sequential(self):
        self.assertGreater(get_primes(500000)["count"], 0)
        self.assertGreater(get_primes(10000000)["count"], 0)
        self.assertGreater(get_primes(400000)["count"], 0)
        self.assertGreater(get_primes(300000)["count"], 0)
        # 6.45s -- sequential, no concurrency

    @concurrent_with_params(500000, 10000000, 400000, 300000)
    def test_concurrent_always(self, n):
        self.assertGreater(get_primes(n, locking="always")["count"], 0)
        # Output:
        # called service with (500000,)
        # allocating:  1 - 500000
        # called service with (10000000,)
        # called service with (400000,)
        # called service with (300000,)
        # allocating:  500000 - 10000000
        # (500000,) >>> 0.6092565059661865
        # (300000,) >>> 5.083366394042969
        # (400000,) >>> 5.098953008651733
        # (10000000,) >>> 6.410214185714722

    @concurrent_with_params(500000, 10000000, 400000, 300000)
    def test_concurrent_optional(self, n):
        self.assertGreater(get_primes(n, locking="optional")["count"], 0)
        # Output:
        # called service with (500000,)
        # allocating:  1 - 500000
        # called service with (10000000,)
        # called service with (400000,)
        # called service with (300000,)
        # allocating:  500000 - 10000000
        # (500000,) >>> 0.6332592964172363
        # (300000,) >>> 0.666248083114624
        # (400000,) >>> 0.7211008071899414
        # (10000000,) >>> 6.694701194763184

