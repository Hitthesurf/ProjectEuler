import unittest
import MathFunctions


class TestMathFunctions(unittest.TestCase):
    def test_factorial_returns_correct_value_for_an_integer(self):
        math_object = MathFunctions.MathFunction()
        self.assertEqual(1, math_object.factorial(1))
        self.assertEqual(2, math_object.factorial(2))
        self.assertEqual(120, math_object.factorial(5))
        self.assertEqual(3628800, math_object.factorial(10))
        self.assertEqual(1, math_object.factorial(0))

    def test_sum_of_individual_digits_for_an_integer_is_correct_value(self):
        math_object = MathFunctions.MathFunction()
        self.assertEqual(9, math_object.add_each_digit(540))
        self.assertEqual(27, math_object.add_each_digit(3628800))


if __name__ == '__main__':
    unittest.main()
