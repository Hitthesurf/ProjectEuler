#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:05:35 2019

@author: pi
"""

import unittest
import primes

class TestCoinSum(unittest.TestCase):
    def test_is_prime_returns_true_when_number_is_prime(self):
        self.assertTrue(primes.is_prime(2))
        self.assertTrue(primes.is_prime(13))

    def test_is_prime_returns_false_when_number_is_not_prime(self):
        self.assertFalse(primes.is_prime(1))
        self.assertFalse(primes.is_prime(15))
        
    def test_prime_at_returns_the_correct_index_of_the_prime(self):
        self.assertEqual(2,primes.prime_at(1))
        self.assertEqual(11,primes.prime_at(5))
    
    def test_prime_workout_returns_correct_numbers(self):
        actual = primes.prime_workout(1, 4, 2)
        expected = [3,5,7,11]
        self.assertEqual(expected, actual)
        
    def test_prime_workout_returns_correct_numbers_2(self):
        actual = primes.prime_workout(1, 3, 4)
        expected = [5,13,17]
        self.assertEqual(expected, actual)
        
    def test_prime_workout_returns_correct_numbers_3(self):
        actual = primes.prime_workout(3, 3, 4)
        expected = [3,7,11]
        self.assertEqual(expected, actual)
        
    def test_mult_prime_core_return_correct_numbers(self):
        actual = primes.mult_prime_core(6, 2)
        expected = [2,3,5,7,11,13,17]
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()