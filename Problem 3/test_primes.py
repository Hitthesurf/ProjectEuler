import unittest
import LargestPrimeFactor


class TestPrimes(unittest.TestCase):
    def test_is_prime_outputs_correct_boolean_value_for_positive_integers(self):
        prime_object = LargestPrimeFactor.Primes()
        self.assertEqual(True, prime_object.is_prime(5))
        self.assertEqual(False, prime_object.is_prime(10))
        self.assertEqual(False, prime_object.is_prime(1))

    def test_prime_factors_outputs_correct_array_for_102(self):
        prime_object = LargestPrimeFactor.Primes()
        self.assertEqual([2, 3, 17], prime_object.prime_factors(102))
        self.assertEqual([3, 3, 3, 37], prime_object.prime_factors(999))
