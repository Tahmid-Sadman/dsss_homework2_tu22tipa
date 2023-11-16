import unittest
from math_quiz import function_random_integer, function_random_operator, function_perform_operation


class TestMathQuiz(unittest.TestCase):

    def test_function_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_operator(self):
        # Test for valid operators returned
        valid_operators = ['+', '-', '*']
        generated_operator = function_random_operator()
        self.assertIn(generated_operator, valid_operators)

    def test_function_perform_operation(self):
        test_cases = [
            (7, 1, '+', '7 + 1', 8),
            (9, 2, '-', '9 - 2', 7),
            (3, 7, '*', '3 * 7', 21),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, ans = function_perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(ans, expected_answer)

if __name__ == "__main__":
    unittest.main()
