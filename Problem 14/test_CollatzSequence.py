import unittest
import CollatzSequence


class TestCollatzSequence(unittest.TestCase):
    def test_even_integers_returns_the_correct_integer_for_next_number(self):
        collatz_object = CollatzSequence.CollatzSequence()
        self.assertEqual(20, collatz_object.next_number(40))

    def test_odd_integers_returns_the_correct_integer_for_next_number(self):
        collatz_object = CollatzSequence.CollatzSequence()
        self.assertEqual(40, collatz_object.next_number(13))

    def test_length_of_sequence_returns_correct_integer_for_given_integer(self):
        collatz_object = CollatzSequence.CollatzSequence()
        self.assertEqual(10, collatz_object.len_of_sequence(13), "The sequence for 13 should contain 10 terms")

    def test_array_of_sequence_returns_correct_array_for_given_integer(self):
        collatz_object = CollatzSequence.CollatzSequence()
        self.assertEqual([13, 40, 20, 10, 5, 16, 8, 4, 2, 1], collatz_object.array_of_sequence(13))

    def test_largest_length_sequence_returns_correct_integer_for_a_given_range(self):
        collatz_object = CollatzSequence.CollatzSequence()
        self.assertEqual(3, collatz_object.largest_length_sequence(1, 5))


if __name__ == '__main__':
    unittest.main()
