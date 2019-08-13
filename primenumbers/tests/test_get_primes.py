from unittest import TestCase

from primenumbers.services.prime_generator import get_primes, get_primes_version_01, get_primes_naive


class TestGetPrimes(TestCase):

    def test_get_primes_01(self):
        self.assertEqual([2, 3], list(get_primes(4)))

    def test_get_primes_02(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(get_primes(30)))

    def test_get_primes_03(self):
        self.assertEqual([11, 13, 17, 19, 23, 29, 31, 37, ], list(get_primes(40, start=10)))

    def test_get_primes_04(self):
        self.assertEqual([], list(get_primes(2)))

    def test_get_primes_05(self):
        self.assertEqual([], list(get_primes(1)))

    def test_get_primes_06(self):
        self.assertEqual([], list(get_primes(-1)))

    def test_get_primes_07(self):
        self.assertEqual([], list(get_primes(10, start=20)))

    def test_get_primes_08(self):
        self.assertEqual([], list(get_primes(10, start=20)))

    def test_get_primes_09(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(get_primes(100, size=10)))

    def test_get_primes_10(self):
        self.assertEqual([31, 37, 41, 43, 47, 53, 59, 61, 67, 71], list(get_primes(100, page=2, size=10)))

    def test_get_primes_l01(self):
        self.assertEqual(168, len(get_primes(1000)))

    def test_get_primes_l01_naive(self):
        self.assertEqual(168, len(get_primes_naive(1000)))  # 5 ms

    def test_get_primes_l02(self):
        self.assertEqual(78498, len(get_primes(1000000)))  # 570 ms

    # def test_get_primes_l02_naive(self):
    #     self.assertEqual(78498, len(get_primes_naive(1000000)))  # stopped after many minutes

    def test_get_primes_l02_old(self):
        self.assertEqual(78498, len(get_primes_version_01(1000000)))  # 570 ms

    def test_get_primes_l02_repeat(self):
        self.assertEqual(78498, len(get_primes(1000000)))  # repeated call 147 ms

    def test_get_primes_l02_section(self):
        self.assertEqual([467, 479, 487, 491, 499, 503, 509, 521, 523, 541],
                         get_primes(1000000, page=10, size=10))  # repetitive call using previous results - 149 ms

    def test_get_primes_l03(self):
        self.assertEqual(78504, len(get_primes(1000100)))  # 148 ms -- utilizes results built from earlier test

    def test_get_primes_l03_old(self):
        self.assertEqual(78504, len(get_primes_version_01(1000100)))  # 563 ms -- does not utilize results built earlier

