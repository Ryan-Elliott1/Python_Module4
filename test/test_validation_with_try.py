import unittest
from input_validation import validation_with_try


class FunctionTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

    def test_average_negative_input2(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)


