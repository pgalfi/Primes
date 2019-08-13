from unittest import TestCase

from primenumbers.generation import get_primes


class TestGetPrimes(TestCase):

    def test_get_primes_01(self):
        self.assertEqual([2, 3], list(get_primes(4)))

    def test_get_primes_02(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(get_primes(30)))

    def test_get_primes_03(self):
        self.assertEqual([11, 13, 17, 19, 23, 29, 31, 37,], list(get_primes(40, start=10)))

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
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(get_primes(100, count=10)))

    def test_get_primes_10(self):
        self.assertEqual([31, 37, 41, 43, 47, 53, 59, 61, 67, 71], list(get_primes(100, count=10, page=2)))

    def test_get_primes_l01(self):
        self.assertEqual(168, len(get_primes(1000)))

    def test_get_primes_l02(self):
        self.assertEqual(78498, len(get_primes(1000000)))  # 570 ms

    def test_get_primes_l03(self):
        self.assertEqual(664579, len(get_primes(10000000)))  # 6s 60 ms
