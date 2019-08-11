from unittest import TestCase
import LexicographicPermutation


class TestPermutation(TestCase):
    def test_find_permutations_for_string_of_length_1_returns_sorted_array_of_strings_holding_all_permutations(self):
        perm_object = LexicographicPermutation.Permutation()
        self.assertEqual(["1"], perm_object.find_permutations("1"))

    def test_find_permutations_for_string_of_length_2_returns_sorted_array_of_strings_holding_all_permutations(self):
        perm_object = LexicographicPermutation.Permutation()
        self.assertEqual(["12", "21"], perm_object.find_permutations("12"))
        self.assertEqual(["12", "21"], perm_object.find_permutations("21"))

    def test_find_permutations_for_string_of_length_3_returns_sorted_array_of_strings_holding_all_permutations(self):
        perm_object = LexicographicPermutation.Permutation()
        self.assertEqual(["012", "021", "102", "120", "201", "210"], perm_object.find_permutations("012"))

    def test_find_permutations_for_string_of_length_4_returns_sorted_array_of_strings_holding_all_permutations(self):
        perm_object = LexicographicPermutation.Permutation()
        self.assertEqual(
            ['1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314', '2341', '2413', '2431', '3124',
             '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312', '4321'],
            perm_object.find_permutations("1234"))

    def test_find_permutation_for_string_have_the_correct_lenght(self):
        perm_object = LexicographicPermutation.Permutation()
        self.assertEqual(6, len(perm_object.find_permutations("123")))
        self.assertEqual(120, len(perm_object.find_permutations("12345")))
        self.assertEqual(5040, len(perm_object.find_permutations("0123456")))
        self.assertEqual(3628800, len(perm_object.find_permutations("0123456789")))
