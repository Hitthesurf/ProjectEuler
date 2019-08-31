#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:25:52 2019

@author: pi
"""

import unittest
import coin_combinations as coin




class TestCoinSum(unittest.TestCase):

    def test_add_number_calculates_correct_total(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [10, 5, 2, 1]
        num_perm.current_perm = [1,0,5,2]
        expected = (1*10)+(0*5)+(5*2)+(2*1)
        actual = num_perm.add_numbers()
        self.assertEqual(expected, actual)

    def test_make_number_creates_the_correct_array(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [10, 5, 2, 1]
        num_perm.make_number()
        expected = [0, 0, 0, 0]
        actual = num_perm.current_perm
        self.assertEqual(expected, actual)
        
    def test_work_out_base_calculates_the_correct_base_values_for_a_given_number(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [20, 10, 5, 2, 1]
        num_perm.current_num = 15
        num_perm.work_out_base()
        expected = [0, 2, 3, 8, 15]
        actual = num_perm.max_base
        self.assertEqual(expected, actual)
        
    def test_add_perm_does_not_add_repeated_combinations(self):
        num_perm = coin.number_permutations()
        num_perm.permutation = [[1,2],[1,3]]
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        actual = num_perm.permutation
        self.assertEqual([[1,2],[1,3]], actual)

    def test_add_perm_adds_the_ordered_combination(self):
        num_perm = coin.number_permutations()
        num_perm.permutations = []
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        actual = num_perm.permutation
        self.assertEqual([[1,2]], actual)
        
    def test_add_perm_does_not_change_current_perm(self):
        num_perm = coin.number_permutations()
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        self.assertEqual([2,1], num_perm.current_perm)
        
    def test_next_number_works_out_the_correct_next_number(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [10, 5, 2, 1]
        num_perm.current_num = 200
        num_perm.max_base = [1, 2, 5, 10]
        num_perm.current_perm = [0, 1, 5, 10]
        num_perm.next_number()
        expected = [0, 2, 0, 0]
        actual = num_perm.current_perm
        self.assertEqual(actual, expected)
    
    def test_perm_number_calculates_the_correct_number_of_combinations(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [1,2,3,4]
        num_perm.perm_number(4)
        actual = num_perm.count_perms
        self.assertEqual(5, actual)
        
    def test_show_permutations_returns_the_correct_permutations(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [10, 5, 2, 1]
        num_perm.permutation = [[1,2,3,0], [2,0,0,6]]
        expected = "1x10 2x5 3x2 0x1 " + "\n"
        expected += "2x10 0x5 0x2 6x1 " + "\n"
        actual = num_perm.show_permutations()
        self.assertEqual(expected, actual)
    
    def test_next_number_can_miss_uneeded_numbers(self):
        num_perm = coin.number_permutations()
        num_perm.only_numbers = [10,5,2,1]
        num_perm.max_base = [1, 2, 5, 10]
        num_perm.current_num = 15
        num_perm.current_perm = [0,2,2,2]
        num_perm.next_number()
        num_perm.next_number()
        expected = [0,2,3,0]
        self.assertEqual(expected, num_perm.current_perm)
        
if __name__ == '__main__':
    unittest.main()