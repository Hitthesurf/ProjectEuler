#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:18:21 2019

@author: pi
"""

import unittest
import coin_sum

class TestCoinSum(unittest.TestCase):

    def test_add_number_calculates_sum_of_all_numbers(self):
        num_perm = coin_sum
        self.assertEqual(15, num_perm.add_numbers([3,2,5,5]))
        
    def test_next_numbers_finds_the_correct_next_number_with_no_carry(self):
        num_perm = coin_sum.number_permutations()
        num_perm.current_perm = [3,2,5,5]
        num_perm.only_numbers = [1,2,3,4,5,6]
        num_perm.next_number()
        actual = num_perm.current_perm
        self.assertEqual([3,2,5,6], actual)
        
    def test_next_numbers_finds_the_correct_next_number_with_a_carry(self):
        num_perm = coin_sum.number_permutations()
        num_perm.current_perm = [5,6,6,6]
        num_perm.only_numbers = [1,2,3,4,5,6]
        num_perm.next_number()
        actual = num_perm.current_perm
        self.assertEqual([6,1,1,1], actual)
        
    def test_next_numbers_finds_the_correct_next_number_with_a_short_carry(self):
        num_perm = coin_sum.number_permutations()
        num_perm.current_perm = [3,2,4,6]
        num_perm.only_numbers = [1,2,3,4,5,6]
        num_perm.next_number()
        actual = num_perm.current_perm
        self.assertEqual([3,2,5,1], actual)
        
    def test_make_number_makes_an_array_with_the_correct_elements_in(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [1,2,3,4,5,6]
        num_perm.current_num = 6
        num_perm.make_number()
        actual = num_perm.current_perm
        self.assertEqual([1,1,1,1,1,1], actual)
        
    def test_max_number_makes_biggest_numbers(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [1,2,3,4,5,6]
        num_perm.current_num = 6
        num_perm.max_number()
        actual = num_perm.max_number()
        self.assertEqual([1,1,1,1,1,1], actual)
        
    def test_check_num_calculates_true_when_sum_of_elements_is_correct_number(self):
        num_perm = coin_sum.number_permutations()       
        num_perm.current_num = 6
        num_perm.current_perm = [0,0,1,2,3]
        self.assertTrue(num_perm.check_num())
        
    def test_check_num_calculates_false_when_sum_of_elements_is_not_correct_number(self):
        num_perm = coin_sum.number_permutations()       
        num_perm.current_num = 6
        num_perm.current_perm = [0,0,1,2,2]
        self.assertFalse(num_perm.check_num())
        
    def test_add_perm_does_not_add_repeated_combinations(self):
        num_perm = coin_sum.number_permutations()
        num_perm.permutation = [[1,2],[1,3]]
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        actual = num_perm.permutation
        self.assertEqual([[1,2],[1,3]], actual)

    def test_add_perm_adds_the_ordered_combination(self):
        num_perm = coin_sum.number_permutations()
        num_perm.permutations = []
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        actual = num_perm.permutation
        self.assertEqual([[1,2]], actual)
        
    def test_add_perm_does_not_change_current_perm(self):
        num_perm = coin_sum.number_permutations()
        num_perm.current_perm = [2,1]
        num_perm.add_perm()
        self.assertEqual([2,1], num_perm.current_perm)
        
    def test_perm_number_calculates_the_correct_number_of_combinations(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [0,1,2,3,4]
        num_perm.perm_number(4)
        actual = num_perm.count_perms
        self.assertEqual(5, actual)
        
    def test_perm_numbers_calculates_correct_permutations(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [0,1,2,3,4]
        num_perm.perm_number(4)
        actual = num_perm.permutation
        expected = []
        expected.append([0, 0, 0, 4])
        expected.append([0, 0, 1, 3])
        expected.append([0, 0, 2, 2])
        expected.append([0, 1, 1, 2])
        expected.append([1, 1, 1, 1])      
        self.assertEqual(expected, actual)
        
    def test_combine_outputs_correct_array(self):
        num_perm = coin_sum
        actual = num_perm.combine([[1,2],[2,2]],[[2,4],[1,4]])
        expected = [[1,2,2,4],[1,1,2,4],[2,2,2,4]]
        self.assertEqual(expected, actual)
        
    def test_delete_duplicates_deletes_all_duplicates(self):
        num_perm = coin_sum
        test_data = [[3,2],[4,1],[4,1],[3,2]]
        actual = num_perm.delete_duplicates(test_data)
        expected = [[3,2], [4,1]]
        self.assertEqual(expected, actual)
        
    def test_inc_combine_includes_last_number(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [0,1,2,5,10,20,50,100,200]
        actual = num_perm.inc_combine([[1]],[[1]])
        expected = [[1,1],[0,2]]
        self.assertEqual(expected, actual)
        
    def test_inc_combine_does_not_include_last_number_when_not_in_array(self):
        num_perm = coin_sum.number_permutations()
        num_perm.only_numbers = [0,1,2,5,10,20,50,100,200]
        test_data = [[0, 2], [1, 1]]
        actual = num_perm.inc_combine(test_data,test_data)
        expected = [[0, 0, 2, 2], [0, 1, 1, 2], [1, 1, 1, 1]]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()